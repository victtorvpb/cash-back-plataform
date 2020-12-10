import logging

from pydantic import EmailStr
from sqlalchemy.orm import Session

from commons.crud.base import CRUDBase
from commons.models.purchase import Purchase
from commons.schemas.purchase import PusrchaseCreate

log = logging.getLogger()


class CRUDPurchase(CRUDBase[Purchase, PusrchaseCreate]):
  
    def create(self, db: Session, *, obj_in: PusrchaseCreate, user_id: int) -> Purchase:
        try:
            log.info(f'create: Creating pursch with code {obj_in.code}')
            db_obj = Purchase(
                code = obj_in.code,
                value = obj_in.value,
                purchase_date = obj_in.purchase_date,
                status = obj_in.status,
                cashback_percente = obj_in.cashback_percente,
                cashback_value = obj_in.cashback_value,
                user_id = user_id
            )
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except Exception:
            log.exception("create: Error on create user")



purchase = CRUDUser(User)