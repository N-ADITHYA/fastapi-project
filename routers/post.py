from fastapi import Depends,status, HTTPException, Response, APIRouter
import schemas
import oauth2
import models
from sqlalchemy.orm import Session
from sqlalchemy_db import get_db
from schemas import for_Create_Post
from typing import List, Optional
from sqlalchemy import func


router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)


@router.get("/", response_model=List[schemas.PostVote])
# @router.get("/")
async def get_posts(Db: Session = Depends(get_db), limit: int = 3, skip: int = 0, search: Optional[str] = ''):
    # posts = db_helper.getting_posts()
    # posts =Db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    result = Db.query(models.Post, func.count(models.Vote.post_id).label("Votes")).join(models.Vote,
                                                                                        models.Vote.post_id == models.Post.id, isouter=True).group_by(
        models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # print(result)
    # data = [row._asdict() for row in result.all()]
    return result


@router.get("/{id}", response_model=schemas.PostVote)
async def return_post_by_id(id: int, Db : Session = Depends(get_db), current_user: str = Depends(
    oauth2.get_Current_User)):
    # post = db_helper.get_posts_by_id(id)
    # if not post:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    # post_query = Db.query(models.Post).filter(models.Post.id == id)

    post_query = Db.query(models.Post, func.count(models.Vote.post_id).label("Votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(
        models.Post.id).filter(models.Post.id == id)
    posts = post_query.first()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Postss)
def create_posts(payload : schemas.PostCreate, Db : Session = Depends(get_db), current_user: int = Depends(
    oauth2.get_Current_User)):
    # new_posts = db_helper.insert_into_db(payload)
    # new_posts = models.Post(title=payload.title, content=payload.content, published=payload.published)

    new_posts = models.Post(owner_id=current_user.id, **payload.dict())

    Db.add(new_posts)
    Db.commit()
    Db.refresh(new_posts)
    return new_posts

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_posts(id: int, response: Response, Db : Session = Depends(get_db), current_user: str = Depends(
    oauth2.get_Current_User)):
    # post = db_helper.delete_post(id)
    post_q = Db.query(models.Post).filter(models.Post.id == id)
    post = post_q.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    post_q.delete(synchronize_session=False)
    Db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Postss)
async def update_posts(id:int, up_pos: for_Create_Post, Db : Session=Depends(get_db), current_user: str = Depends(
    oauth2.get_Current_User)):
    # update_posts = db_helper.updating_rows(id,payload)

    post_query = Db.query(models.Post).filter(models.Post.id == id)

    payload = post_query.first()
    if payload == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post_query.update(up_pos.dict(), synchronize_session=False)

    if payload.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    Db.commit()

    return post_query.first()
