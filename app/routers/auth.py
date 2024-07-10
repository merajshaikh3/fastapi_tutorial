from fastapi import FastAPI, Response, status, HTTPException, Depends
from .. import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from typing import List
from ..database import engine, get_db
from fastapi import APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(
                    prefix = "/login",
                    tags = ['Authentication']
                  )


@router.post("", status_code=status.HTTP_201_CREATED, response_model = schemas.Token)
def login_users(input_user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    print(type(input_user))
    output_user = db.query(models.User).filter(models.User.email == input_user.username).first() #
    print(output_user.email)
    print(output_user.password)
    print(output_user.id)
    # print(type(user_name))

    if not output_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail = f"INVALID CREDENTIALS")
    
    verification_status = utils.verify(input_user.password, output_user.password) # note that the hashing needs to be done from the same library
    # print(verification_status) -> will either give True or False

    if not verification_status:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail = f"INVALID CREDENTIALS")
    
    access_token = oauth2.create_access_token(data={"user_id":output_user.id, "email_id": output_user.email})

    return {"access_token": access_token, "token_type": "bearer"}