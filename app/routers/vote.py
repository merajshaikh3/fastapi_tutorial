from fastapi import FastAPI, Response, status, HTTPException, Depends
from .. import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database import engine, get_db
from fastapi import APIRouter

router = APIRouter(
                    prefix = "/votes",
                    tags = ['Votes']
                  )


@router.post("", status_code=status.HTTP_201_CREATED)
def give_vote(vote: schemas.Vote, db: Session = Depends(get_db), curr_user: models.User = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {vote.post_id} does not exist")
    
    user_existing_vote = db.query(models.Vote).filter(models.Vote.post_id==vote.post_id, models.Vote.user_id==curr_user.id).first()

    # print(user_existing_vote)

    if vote.dir == 1:
        if user_existing_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"post has already been liked")
        else:
            new_vote = models.Vote(post_id=vote.post_id, user_id=curr_user.id)
            db.add(new_vote)
            db.commit()
            db.refresh(new_vote)
            return {"message":"successfully liked post"}
    else:
        if not user_existing_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cannot undo like on a post that has not been liked!")
        else:
            user_existing_vote.delete(synchronize_session=False)
            db.commit()
            return {"message":"successfully unliked post"}

