from typing import Optional

from pydantic import EmailStr, constr

from commons.schemas.base import SchemaBase, SchemaInDBBase, UUID


class UserBase(SchemaBase):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    cpf: Optional[constr(max_length=14)] = None


class UserCreate(UserBase):
    full_name: str
    email: EmailStr
    password: str
    cpf: constr(max_length=14)


class UserInDBBase(SchemaInDBBase):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    cpf: Optional[constr(max_length=14)]
    is_active: bool = None
    uuid: Optional[UUID] = None


class User(UserInDBBase):
    pass


class UserInDB(SchemaInDBBase):
    hashed_password: str
