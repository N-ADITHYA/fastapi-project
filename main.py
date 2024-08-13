from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from sqlalchemy_db import get_db
from routers import post, user, auth, vote

from fastapi.middleware.cors import CORSMiddleware

# from sqlalchemy_db import engine
''' since we have alembic, we no longer need this code which tells sqlalchemy to create tables from the models.py module'''
# models.Base.metadata.create_all(bind=engine)

origins = ['*']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']

)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get('/')
def hello():
    return {'Message': 'Successfully deployed to Ubuntu!!!!!!'}

@app.get('/sqlalchemy')
async def test_posts(Db : Session = Depends(get_db)):
    posts = Db.query(models.Post).all()
    print(posts)
    return {"message": posts}
























