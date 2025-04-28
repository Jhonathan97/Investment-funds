import boto3
import os

sns_client = boto3.client('sns', region_name='us-east-1')

TOPIC_EMAIL_ARN = os.getenv("EMAIL_TOPIC_ARN")
PHONE_NUMBER = "+573147693464"

def send_notification(preference, fund_name):
    
    message = f"Te has suscrito exitosamente al fondo {fund_name}"
    
    try:
        if preference == "email":
            if not TOPIC_EMAIL_ARN:
                print("⚠️ EMAIL_TOPIC_ARN no está configurado. No se envió el email.")
            else:
                sns_client.publish(
                    TopicArn=TOPIC_EMAIL_ARN,
                    Message=message,
                    Subject="Suscripción a fondo de inversión"
                )
                print(f"Correo de suscripción enviado al fondo {fund_name}")

        elif preference == "sms":
            sns_client.publish(
                PhoneNumber=PHONE_NUMBER,
                Message=message
            )
            print(f"SMS de suscripción enviado al fondo {fund_name}")

        elif preference == "both":
            if not TOPIC_EMAIL_ARN:
                print("EMAIL_TOPIC_ARN no está configurado. Solo se enviará SMS.")
            else:
                sns_client.publish(
                    TopicArn=TOPIC_EMAIL_ARN,
                    Message=message,
                    Subject="Suscripción a fondo de inversión"
                )
            sns_client.publish(
                PhoneNumber=PHONE_NUMBER,
                Message=message
            )
            print(f"Correo y SMS de suscripción enviados al fondo {fund_name}")

        else:
            raise Exception("Preferencia de notificación inválida")

    except Exception as e:
        print(f"Error enviando notificación: {str(e)}")
