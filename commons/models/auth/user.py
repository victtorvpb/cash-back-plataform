from sqlalchemy import Column, String, Boolean

from commons.db.base_class import SQLAlchemyBaseModel


class User(SQLAlchemyBaseModel):

    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    cpf = Column(String(14), nullable=False, unique=True)
    full_name = Column(String, nullable=False)
