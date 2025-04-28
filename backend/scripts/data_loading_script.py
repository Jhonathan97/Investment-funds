import boto3

# Conectar a DynamoDB
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
balance_table = dynamodb.Table('Balance')
fund_table = dynamodb.Table('Fund')  # <--- tu nueva tabla Fund

# Fondos iniciales a cargar
funds_init = [
    {
        "id": "1",
        "name": "FPV_EL CLIENTE_RECAUDADORA",
        "min_amount": 75000,
        "category": "FPV"
    },
    {
        "id": "2",
        "name": "FPV_EL CLIENTE_ECOPETROL",
        "min_amount": 125000,
        "category": "FPV"
    },
    {
        "id": "3",
        "name": "DEUDAPRIVADA",
        "min_amount": 50000,
        "category": "FIC"
    },
    {
        "id": "4",
        "name": "FDO_ACCIONES",
        "min_amount": 250000,
        "category": "FIC"
    },
    {
        "id": "5",
        "name": "FPV_EL CLIENTE_DINAMICA",
        "min_amount": 100000,
        "category": "FPV"
    },
]

def load_funds():
    for fund in funds_init:
        try:
            fund_table.put_item(Item=fund)
            print(f"Fondo '{fund['name']}' cargado exitosamente.")
        except Exception as e:
            print(f"Error al cargar fondo '{fund['name']}': {e}")
            
def initialize_balance():
    try:
        balance_table.put_item(
            Item={
                "id": "single_user",
                "amount": 500000
            }
        )
        print("✅ Balance inicializado correctamente (500,000 COP)")
    except Exception as e:
        print(f"Error inicializando el balance: {e}")


if __name__ == "__main__":
    initialize_balance()
    load_funds()
