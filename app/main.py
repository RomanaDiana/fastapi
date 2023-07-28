from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth
from .config import settings

#models.Base.metadata.create_all(bind=engine)
# #told sqlalchemy to run the create statements so it generated all the tables
# when it first started up
# dont need it cause of alembic

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            #{"title": "favorite foods", "content": "I like pizza", "id": 2}]

#def find_post(id):
    #for p in my_posts:
        #if p ["id"] == id:
            #return p
        

#def find_index_post(id):
    #for i, p in enumerate(my_posts):
         #if p['id'] == id:
            #return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello World"}  #don't need, but leave it be




