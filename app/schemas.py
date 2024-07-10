# schemas/Pydantic models define the structure of a request & response

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, Literal

class UserBase(BaseModel):
    email: EmailStr
    id: int

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    created_at: datetime

    # The below code will handle API response which at times can be an ORM object
    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    """
    Link: https://fastapi.tiangolo.com/tutorial/sql-databases/
    Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).

    This way, instead of only trying to get the id value from a dict, as in:


    id = data["id"]

    it will also try to get it from an attribute, as in:

    id = data.id
    """
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str # will have the encoded token
    token_type: str # will have 'bearer'

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: Literal[0,1]


