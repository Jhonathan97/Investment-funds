from fastapi import APIRouter
from app.services import fund_service

router = APIRouter()

@router.get("/")
async def get_history():
    return fund_service.get_history()
