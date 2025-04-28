from pydantic import BaseModel
from typing import Literal

class FundSuscriptionRequest(BaseModel):
    fund_id: str
    notification_preference: Literal["email", "sms", "both"]

class FundCancelRequest(BaseModel):
    fund_id: str


