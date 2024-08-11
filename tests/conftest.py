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
from oauth2 import create_tokens
import models

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

@pytest.fixture
def test_user(client):
    user_data = {"email": "adithya@example.com",
                 "password": "123",}
    res = client.post("/users", json=user_data)
    assert res.status_code == 201
    print(res.json())
    new_user = res.json()
    new_user["password"] = user_data['password']
    return new_user

@pytest.fixture
def token(test_user):
    return create_tokens({"user_id": test_user['id']})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client

@pytest.fixture
def test_posts(test_user, session):
    posts_data = [{
        "title": "first post",
        "content": "first post",
        "owner_id": test_user['id']
    },{
        "title": "second post",
        "content": "second post",
        "owner_id": test_user['id']
    },{
        "title": "third post",
        "content": "third post",
        "owner_id": test_user['id']
    }]
    def create_posts_model(post):
        return models.Post(**post)
    posts_map = map(create_posts_model, posts_data)
    posts = list(posts_map)

    session.add_all(posts)
    # session.add_all([models.Post(title="first title", content="first content", owner_id=test_user['id'])])
    session.commit()

    posts = session.query(models.Post).all()
    return posts