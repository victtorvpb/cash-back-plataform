from typing import Optional
from datetime import datetime

from pydantic import validator

from commons.schemas.base import SchemaBase


class PusrchaseBase(SchemaBase):
    code: Optional[str] = None
    value: float = None
    purchase_date: datetime = None


class PusrchaseCreate(PusrchaseBase):
    code: Optional[str]
    value: float
    purchase_date: datetime
    status: str

    @validator('status')
    def check_status_in(cls, v):
        if v in ('pending', 'valid'):
            return v

        raise ValueError("status in not valid")
