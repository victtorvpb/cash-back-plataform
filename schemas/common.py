from schemas.base import PydanticBase


class Message(PydanticBase):
    status: str


class HTTPException(PydanticBase):
    detail: str

    class Config:
        stitle = 'asdasda'
