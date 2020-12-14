import logging

from typing import Optional

from pydantic import EmailStr
from sqlalchemy.orm import Session
from sqlalchemy import or_

from commons.utils.security import get_password, verify_password
from commons.crud.base import CRUDBase
from commons.models.auth.user import User
from commons.schemas.auth.user import UserCreate
from commons.utils.format import format_cpf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CRUDUser(CRUDBase[User, UserCreate]):
    def get_by_email_or_cpf(self, db: Session, email: EmailStr, cpf: str) -> Optional[User]:
        try:
            return (
                db.query(self.model)
                .filter(or_(self.model.email == email, self.model.cpf == format_cpf(cpf)))
                .first()
            )
        except Exception:
            extra = {"email": email, "cpf": cpf}
            logger.exception("get_by_email_or_cpf: Error to get user by Email or CPF", extra=extra)

    def get_by_email(self, db: Session, email: EmailStr) -> Optional[User]:
        try:
            return db.query(self.model).filter(self.model.email == email).first()
        except Exception:
            extra = {"email": email}
            logger.exception("get_by_email: Error to get user by Email", extra=extra)

    def get_by_cpf(self, db: Session, cpf: str) -> Optional[User]:
        try:
            return db.query(self.model).filter(self.model.cpf == cpf).first()
        except Exception:
            extra = {"cpf": cpf}
            logger.exception("get_by_cpf: Error to get user by CPF", extra=extra)

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        try:
            db_obj = User(
                full_name=obj_in.full_name,
                email=obj_in.email,
                hashed_password=get_password(obj_in.password),
                cpf=format_cpf(obj_in.cpf),
            )
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except Exception:
            logger.exception("create: Error on create user")

    def authenticate(self, db: Session, *, email: EmailStr, password: str):
        user = self.get_by_email(db, email=email)

        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None

        return user


user = CRUDUser(User)
