from typing import Optional
from datetime import datetime
from uuid import UUID
from enum import Enum

from commons.schemas.base import SchemaBase, SchemaInDBBase


class StatusEnum(str, Enum):
    approved = "approved"
    pending = "pending"


class PurchaseBase(SchemaBase):
    code: Optional[str] = None
    value: Optional[float] = None
    purchase_date: Optional[datetime] = None


class PurchaseCreate(PurchaseBase):
    code: str
    value: float
    purchase_date: datetime
    cpf: str


class PurchaseInDBBase(SchemaInDBBase):
    code: Optional[str] = None
    value: Optional[float] = None
    purchase_date: datetime = None
    uuid: Optional[UUID] = None
    cashback_percente: Optional[float] = None
    cashback_value: Optional[float] = None
    status: Optional[StatusEnum] = StatusEnum.pending


class Pusrchase(PurchaseInDBBase):
    pass


class PurcahseCredit(SchemaBase):
    credit: int = None


class PurchaseCreditRequest(SchemaBase):

    statusCode: int
    body: PurcahseCredit
