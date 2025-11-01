from sqlalchemy.orm import Session
from fastapi import status, Response
from ..models import models, schemas

def create(db: Session, sandwich: schemas.SandwichCreate):
    obj = models.Sandwich(**sandwich.model_dump()); db.add(obj); db.commit(); db.refresh(obj); return obj

def read_all(db: Session): return db.query(models.Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update(db: Session, sandwich_id: int, sandwich: schemas.SandwichUpdate):
    q = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    q.update(sandwich.model_dump(exclude_unset=True), synchronize_session=False); db.commit(); return q.first()

def delete(db: Session, sandwich_id: int):
    db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).delete(synchronize_session=False); db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)