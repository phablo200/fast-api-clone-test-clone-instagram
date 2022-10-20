from sqlalchemy.orm import Session
from datetime import datetime

from db.models import DbComment
from routers.schemas import CommentBase

def get_all(db: Session, post_id: int):
  return db.query(DbComment).filter(DbComment.id == post_id).all()

def create(db: Session, request: CommentBase):
  new_comment = DbComment(
    text = request.text,
    username = request.username,
    timestamp = datetime.now(),
    post_id = request.post_id
  )
  
  db.add(new_comment)
  db.commit()
  db.refresh(new_comment)
  return new_comment