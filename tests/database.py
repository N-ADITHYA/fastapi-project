from fastapi.testclient import TestClient
from main import app
import schemas
from Config import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_db import get_db
from sqlalchemy_db import Base
import pytest


SQLALCHEMY_db_URL = f'postgresql+psycopg2://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}_test'
engine = create_engine(SQLALCHEMY_db_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    print("My session fixture ran")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Db = TestingSessionLocal()
    try:
        yield Db
    finally:
            Db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

