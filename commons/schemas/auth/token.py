from typing import Optional

from pydantic import BaseModel
from commons.schemas.base import SchemaBase


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(SchemaBase):
    sub: Optional[int] = None
