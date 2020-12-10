from sqlalchemy import Column, String, Numeric, DateTime, Float

from commons.db.base_class import SQLAlchemyBaseModel

class Purchase(SQLAlchemyBaseModel):

    code = Column(String, nullable=False, unique=True, index=True)
    value = Column(Numeric, nullable=False, default = 0)
    purchase_date = Column(DateTime)
    status = Column(String, nullable=False, unique=True, index=True)
    cashback_percente = Column(Float)
    cashback_value = Column(Numeric, nullable=False, default = 0)