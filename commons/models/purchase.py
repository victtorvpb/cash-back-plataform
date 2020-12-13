from sqlalchemy import Column, String, Numeric, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship, validates

from commons.db.base_class import SQLAlchemyBaseModel
from commons.schemas import StatusEnum


class Purchase(SQLAlchemyBaseModel):

    code = Column(String, nullable=False, unique=True, index=True)
    value = Column(Numeric, nullable=False, default=0.0)
    purchase_date = Column(DateTime)
    status = Column(String, nullable=False)
    cashback_percente = Column(Float)
    cashback_value = Column(Numeric, nullable=False, default=0.0)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", backref="purchases_itens")

    @validates('stauts')
    def validate_status(self, key, status):

        assert status in StatusEnum.__members__.keys()
        return status
