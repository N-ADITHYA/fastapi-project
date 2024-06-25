from fastapi import status, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import sqlalchemy_db
import schemas
import oauth2
import models

router = APIRouter(
    prefix = '/vote',
    tags = ['Votes']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def votes(vote: schemas.vote, Db: Session = Depends(sqlalchemy_db.get_db), current_user: str = Depends(
    oauth2.get_Current_User)):

    post = Db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    vote_query = Db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_post = vote_query.first()
    if vote.dir == 1:
        if found_post:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Vote {vote.post_id} already posted')
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        Db.add(new_vote)
        Db.commit()
        return {"Message":"Vote added successfully"}
    else:
        if not found_post:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Post not found")
        vote_query.delete(synchronize_session=False)
        Db.commit()
        return {"Message":"Vote deleted successfully"}