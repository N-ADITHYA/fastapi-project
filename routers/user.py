from utils import hash
import schemas
import models
from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy_db import  get_db

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get("/")
def getT_user(Db: Session = Depends(get_db)):
    userss = Db.query(models.User).all()
    return userss



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Userout)
def create_user(user : schemas.UserCreate, Db : Session = Depends(get_db)):

    hashed_password = hash(user.password)
    user.password = hashed_password
    created_data = models.User(**user.dict())
    Db.add(created_data)
    Db.commit()
    Db.refresh(created_data)
    return created_data

@router.get("/{id}", response_model=schemas.Userout)
def user_by_id(id: int, Db: Session = Depends(get_db)):
    user = Db.query(models.User).filter(models.User.id == id).first()

    if  not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user

