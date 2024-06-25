from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import utils
import schemas
import oauth2
import models
from sqlalchemy_db import get_db

router = APIRouter(
    tags=['Authentication']
)


@router.post('/signup', response_model=schemas.UserCreate)
def signup(userAcc: schemas.UserCreate, Db: Session = Depends(get_db)):
    try:
        hashed_password = utils.hash(userAcc.password)
        userAcc.password = hashed_password
        userdata_dict = models.User(**userAcc.dict())
        Db.add(userdata_dict)
        Db.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED)


    return userdata_dict
@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), Db: Session = Depends(get_db)):
    user_det = Db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user_det:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Authentication credentials were not satisfied')

    if not utils.verify(user_credentials.password, user_det.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Authentication credentials were not satisfied')


    access_token = oauth2.create_tokens(data= {"User_id":user_det.id})

    return {"access_token": access_token, "token_type": "bearer"}