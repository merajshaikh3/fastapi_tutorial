from fastapi import FastAPI, Response, status, HTTPException, Depends
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from typing import List
from ..database import engine, get_db
from fastapi import APIRouter

router = APIRouter(
                    prefix = "/users",
                    tags = ['Users']
                  )

@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    # generating password hash and replacing the password with its hash value
    password_hash = utils.get_password_hash(user.password)
    user.password = password_hash

    # Currently the data provided by the user is stored in a Pydantic model. 'model_dump()' will convert that to a
    # The hashing is a one way process. Even if the company wants they cannot reverse engineer it
    new_user = models.User(**user.model_dump()) # Instantiating the 'User' table
    db.add(new_user)
    db.commit()
    db.refresh(new_user) # new_post is an SQLAlchemy model and not a dictionary - add print statements to check out its type

    return new_user

@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"user with id {id} was not found")
    return user


