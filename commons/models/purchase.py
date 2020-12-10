from sqlalchemy import Column, String, Numeric, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import  relationship

from commons.db.base_class import SQLAlchemyBaseModel

class Purchase(SQLAlchemyBaseModel):

    code = Column(String, nullable=False, unique=True, index=True)
    value = Column(Numeric, nullable=False, default = 0)
    purchase_date = Column(DateTime)
    status = Column(String, nullable=False, unique=True, index=True)
    cashback_percente = Column(Float)
    cashback_value = Column(Numeric, nullable=False, default = 0)
    user_id = partner_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    partner = relationship("User", backref="purchases_itens")