from fastapi import APIRouter, HTTPException
from app.schemas.funds import FundSuscriptionRequest, FundCancelRequest
from app.services import fund_service

router = APIRouter()

@router.get("/")
async def get_funds():
    return fund_service.get_funds()


@router.post("/subscribe")
async def subscribe(request: FundSuscriptionRequest):
    try:
        return fund_service.subscribe(request)
    except HTTPException as e:
        raise e

@router.post("/cancel")
async def cancel(request: FundCancelRequest):
    try:
        return fund_service.cancel_subscription(request)
    except HTTPException as e:
        raise e

