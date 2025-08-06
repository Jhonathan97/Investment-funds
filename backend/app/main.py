from mangum import Mangum

from fastapi import FastAPI
from app.api import funds, history
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Investment fund platform",
    description="A platform for managing investment funds",
    version="0.0.1",
)

handler = Mangum(app)
#  Configurar CORS 
origins = [
    "http://localhost:5173",
    "http://investment-funds-stack-frontendbucket-vxbxljf7dp4u.s3-website-us-east-1.amazonaws.com",
    "https://investment-funds-stack-frontendbucket-vxbxljf7dp4u.s3-website-us-east-1.amazonaws.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,               # Lista de dominios permitidos
    allow_credentials=True,              # Permitir cookies / headers especiales
    allow_methods=["*"],                  # Permitir todos los métodos (GET, POST, PUT, DELETE...)
    allow_headers=["*"],                  # Permitir todas las cabeceras
)

app.include_router(funds.router, prefix="/funds", tags=["funds"])
app.include_router(history.router, prefix="/history", tags=["history"])