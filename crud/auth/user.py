from typing import Optional

from pydantic import EmailStr
from sqlalchemy.orm import Session
from sqlalchemy import or_

from commons.security import get_password, verify_password
from crud.base import CRUDBase
from models.auth.user import User
from schemas.auth.user import UserCreate


class CRUDUser(CRUDBase[User, UserCreate]):
    def get_by_email_or_cpf(self, db: Session, email: EmailStr, cpf: str) -> Optional[User]:
        return (
            db.query(self.model)
            .filter(or_(self.model.email == email, self.model.cpf == cpf))
            .first()
        )

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            full_name=obj_in.full_name,
            email=obj_in.email,
            hashed_password=get_password(obj_in.password),
            cpf=obj_in.cpf,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(self, db: Session, *, email: EmailStr, password: str):
        user = self.get_by_email(db, email=email)

        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None

        return user


user = CRUDUser(User)
