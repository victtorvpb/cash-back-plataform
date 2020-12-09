from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from commons.config import settings as stg

engine = create_engine(stg.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
