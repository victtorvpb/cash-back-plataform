from typing import Optional
from uuid import UUID

from pydantic import EmailStr, constr, validator
from validate_docbr import CPF

from commons.schemas.base import SchemaBase, SchemaInDBBase


class UserBase(SchemaBase):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    cpf: Optional[constr(max_length=14)] = None

    @validator('cpf')
    def cpf_validator(cls, v):
        cpf = CPF()

        if not cpf.validate(v):
            raise ValueError('Invalid CPF')

        return v


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

    @validator('cpf')
    def cpf_validator(cls, v):
        cpf = CPF()

        if not cpf.validate(v):
            raise ValueError('Invalid CPF')

        return v


class User(UserInDBBase):
    pass
