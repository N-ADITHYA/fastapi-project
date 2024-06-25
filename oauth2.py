from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import schemas
from sqlalchemy.orm import Session
from sqlalchemy_db import get_db
import models
from Config import setting

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


SECRET_KEY = f'{setting.secret_key}'
ALGORITHM = setting.algorithm
Time_at_expiration = setting.time_at_expiration

def create_tokens(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=Time_at_expiration)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_Access_Token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("User_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data
def get_Current_User(token: str = Depends(oauth2_scheme), Db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Not Authenticated",
                                          headers=({"WWW-AUTHENTICATE": "Bearer"}))

    token = verify_Access_Token(token, credentials_exception)
    current_user = Db.query(models.User).filter(models.User.id == token.id).first()
    return current_user
