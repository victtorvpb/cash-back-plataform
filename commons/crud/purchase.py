import logging

from sqlalchemy.orm import Session

from commons.crud.base import CRUDBase
from commons.models.purchase import Purchase
from commons.schemas.purchase import PurchaseCreate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CRUDPurchase(CRUDBase[Purchase, PurchaseCreate]):
    def create(
        self, db: Session, *, obj_in: PurchaseCreate, user_id: int, request_uuid: str
    ) -> Purchase:

        try:
            extra = {"code": obj_in.code, "request_uuid": request_uuid}
            if obj_in.cpf == '153.509.460-56':
                status = 'approved'
            else:
                status = 'pending'

            cashback_value, cashback_percente = self.calculate_purchase_percentil(obj_in.value)

            logger.info(f'create: Creating pursch with code {obj_in.code}', extra=extra)
            db_obj = Purchase(
                code=obj_in.code,
                value=obj_in.value,
                purchase_date=obj_in.purchase_date,
                status=status,
                cashback_percente=cashback_percente,
                cashback_value=cashback_value,
                user_id=user_id,
            )
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except Exception:
            logger.exception("create: Error on create user", extra=extra)
            raise

    def get_purchase_by_code(self, db: Session, *, code: str, request_uuid: str) -> bool:
        try:
            purchase = db.query(self.model).filter(self.model.code == code).first()
            if purchase:
                return True

            return False

        except Exception:
            extra = {"code": code, "request_uuid": request_uuid}
            logger.exception("get_purchase_by_code: erro on get purchase", extra=extra)

    def calculate_purchase_percentil(self, value_purchase: float) -> tuple:

        if 0 < value_purchase < 1000:
            return (value_purchase * 0.10, 10)
        elif 1000 <= value_purchase <= 1500:
            return (value_purchase * 0.15, 15)
        elif 1500 < value_purchase:
            return (value_purchase * 0.20, 20)

        return (0, 0)


purchase = CRUDPurchase(Purchase)
