import pytest
import schemas
from jose import jwt
from Config import setting



# def test_root(client):
#     res = client.get("/")
#     print(res.json().get("Message"))
#     assert res.json().get("Message") == "bind mount works well !!!!!"
#     assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users", json={"email": "hellow@example.com", "password": "123"})

    new_user = schemas.Userout(**res.json())
    assert new_user.email == "hellow@example.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post(
        "/login", data={"username": test_user['email'], "password": test_user['password']}
    )
    print(res.json())
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, setting.secret_key, algorithms=[setting.algorithm])
    id: str = payload.get("User_id")
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code",[
    ("wwww@fv", "2132", 403)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    assert res.status_code == status_code
    # assert res.json().get('detail') == "Authentication credentials were not satisfied"