from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Config import setting

SQLALCHEMY_db_URL = setting.sqlalchemy_db_url
engine = create_engine(SQLALCHEMY_db_URL, pool_size=10, max_overflow=20, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Dependency
def get_db():
    Db = SessionLocal()
    try:
        yield Db
    finally:
        Db.close()
