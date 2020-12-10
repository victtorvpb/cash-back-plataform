from typing import Optional

from commons.schemas.base import SchemaBase


class Token(SchemaBase):
    access_token: str
    token_type: str


class TokenPayload(SchemaBase):
    sub: Optional[int] = None
