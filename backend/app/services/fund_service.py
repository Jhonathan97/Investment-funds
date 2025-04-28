import uuid
from fastapi import HTTPException
from app.utils import helpers
from app.services import notification_service
import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Conexión DynamoDB
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

FUND_TABLE = dynamodb.Table('Fund')
TRANSACTION_TABLE = dynamodb.Table('Transaction')
BALANCE_TABLE = dynamodb.Table('Balance')

def get_funds():
    try:
        response = FUND_TABLE.scan()
        return response.get('Items', [])
    except (BotoCoreError, ClientError) as e:
        print(f"Error obteniendo fondos: {str(e)}")
        raise HTTPException(status_code=500, detail="Error accediendo a los fondos en base de datos.")

def get_history():
    try:
        response = TRANSACTION_TABLE.scan()
        return response.get('Items', [])
    except (BotoCoreError, ClientError) as e:
        print(f"Error obteniendo historial: {str(e)}")
        raise HTTPException(status_code=500, detail="Error accediendo al historial en base de datos.")

def subscribe(request):
    print("llego al subscribe "+ request.fund_id)
    try:
        # Buscar fondo
        fund_response = FUND_TABLE.get_item(Key={'id': request.fund_id})
        fund = fund_response.get('Item')
        if not fund:
            raise HTTPException(status_code=404, detail="Fondo no encontrado.")

        # Consultar saldo
        balance_response = BALANCE_TABLE.get_item(Key={'id': 'single_user'})
        print("balance_response " + str(balance_response))

        balance_data = balance_response.get('Item')
        if not balance_data or 'amount' not in balance_data:
            raise HTTPException(status_code=500, detail="Saldo no encontrado o inválido.")

        current_balance = balance_data['amount']
        if current_balance < fund['min_amount']:
            raise HTTPException(
                status_code=400,
                detail=f"No tiene saldo disponible para vincularse al fondo {fund['name']}."
            )

        # Actualizar saldo
        new_balance = current_balance - fund['min_amount']
        BALANCE_TABLE.put_item(Item={'id': 'single_user', 'amount': new_balance})

        # Registrar transacción
        transaction_id = str(uuid.uuid4())
        TRANSACTION_TABLE.put_item(Item={
            'transaction_id': transaction_id,
            'type': 'subscribe',
            'fund_id': fund['id'],
            'fund_name': fund['name'],
            'amount': fund['min_amount'],
            'date': helpers.current_date(),
            'notification_sent': False,
        })

        # Enviar notificación (no romper si falla)
        try:
            notification_service.send_notification(request.notification_preference, fund['name'])
        except Exception as notify_error:
            print(f"⚠️ Error enviando notificación: {str(notify_error)}")

        return {
            "message": f"Suscrito exitosamente al fondo {fund['name']}.",
            "transaction_id": transaction_id
        }

    except (BotoCoreError, ClientError) as e:
        print(f"Error de AWS Boto3: {str(e)}")
        raise HTTPException(status_code=500, detail="Error en acceso a base de datos.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor.")

def cancel_subscription(request):
    try:
        # Buscar fondo
        fund_response = FUND_TABLE.get_item(Key={'id': request.fund_id})
        fund = fund_response.get('Item')
        if not fund:
            raise HTTPException(status_code=404, detail="Fondo no encontrado.")

        # Consultar saldo actual
        balance_response = BALANCE_TABLE.get_item(Key={'id': 'single_user'})
        balance_data = balance_response.get('Item')
        if not balance_data or 'amount' not in balance_data:
            raise HTTPException(status_code=500, detail="Saldo no encontrado o inválido.")

        current_balance = balance_data['amount']

        # Actualizar saldo sumando el monto del fondo
        new_balance = current_balance + fund['min_amount']
        BALANCE_TABLE.put_item(Item={'id': 'single_user', 'amount': new_balance})

        # Registrar transacción
        TRANSACTION_TABLE.put_item(Item={
            'transaction_id': str(uuid.uuid4()),
            'type': 'cancel',
            'fund_id': fund['id'],
            'fund_name': fund['name'],
            'amount': fund['min_amount'],
            'date': helpers.current_date(),
        })

        return {"message": f"Cancelado exitosamente el fondo {fund['name']}"}

    except (BotoCoreError, ClientError) as e:
        print(f"Error de AWS Boto3: {str(e)}")
        raise HTTPException(status_code=500, detail="Error en acceso a base de datos.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor.")
