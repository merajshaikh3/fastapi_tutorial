#To run a uvicorn file from a folder named 'app' => uvicorn app.main:app --reload
#You need psycopg to run a sql code on a database ('psycopg' is a database driver)
#SQLAlchemy does not understand SQL
#We have created a table using sqlalchemy. Everytime we save the file it checks for the table 'posts'. If it finds it, then it does nothing. Else it will create a new table by the name of 'posts'
# start from 5:32:00

from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins=["https://www.google.com", "https://www.youtube.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def dummy_request():
    return {"message": "Hello World"} 