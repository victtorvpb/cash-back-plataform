from datetime import datetime
from uuid import UUID as UUID_TYPE, uuid4

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.dialects.postgresql import UUID


@as_declarative()
class Base:
    id: int
    created_at: datetime
    updated_at: datetime
    uuid: UUID_TYPE
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class SQLAlchemyBaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.utcnow)

    uuid = Column(UUID(as_uuid=True), nullable=False, unique=True, default=uuid4)
