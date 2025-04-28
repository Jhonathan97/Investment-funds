# Plataforma de Fondos de Inversión

## Descripción

Aplicación web para gestionar suscripciones y cancelaciones de fondos de inversión, con notificaciones por email o SMS.

## Tecnologías
- Backend: FastAPI, Python, DynamoDB, SNS, Lambda, API Gateway.
- Frontend: React.js.
- Infraestructura como código: AWS CloudFormation.

## Funcionalidades
- Suscripción a fondos.
- Cancelación de fondos.
- Visualización de historial de transacciones.
- Notificaciones por Email/SMS.

## Esquema de Base de Datos (NoSQL)

Tablas DynamoDB:
- **Fund**: fondos disponibles.
- **Transaction**: historial de transacciones.
- **Balance**: saldo actual del usuario.

## Despliegue

### Backend

1. Crear los recursos con el archivo `cloudformation.yaml`.
2. Empaquetar el backend (`backend-code.zip`) y subirlo a S3.
3. Actualizar la función Lambda.
4. Crear API Gateway HTTP API (Proxy integration).
5. Conectar Lambda a API Gateway.

### Frontend

1. Build del proyecto React.
2. Subir a S3 público (bucket estático).
3. Asociar endpoint de S3 como frontend.


## Estructura de proyecto

investment-fund-challenge/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   ├── env/ (virtualenv)
│   ├── backend_build/ (para Lambda ZIP)
│   └── scripts/
│       └── data_loading_script.py
├── frontend/
│   ├── src/
│   ├── public/
│   └── vite.config.js
├── infrastructure.yaml
│ 
└── README.md

## Instrucciones de despliegue
Crear stack con CloudFormation:

```bash
aws cloudformation deploy --template-file infrastructure/cloudformation.yaml --stack-name investment-fund-challenge --capabilities CAPABILITY_NAMED_IAM
```
## Inicialización de datos

Correr script para cargar fondos y saldo inicial en DynamoDB.

```bash
python scripts/data_loading_script.py
```

