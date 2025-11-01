from sqlalchemy.orm import Session
from fastapi import status, Response
from ..models import models, schemas

def create(db: Session, resource: schemas.ResourceCreate):
    obj = models.Resource(**resource.model_dump()); db.add(obj); db.commit(); db.refresh(obj); return obj

def read_all(db: Session): return db.query(models.Resource).all()

def read_one(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

def update(db: Session, resource_id: int, resource: schemas.ResourceUpdate):
    q = db.query(models.Resource).filter(models.Resource.id == resource_id)
    q.update(resource.model_dump(exclude_unset=True), synchronize_session=False); db.commit(); return q.first()

def delete(db: Session, resource_id: int):
    db.query(models.Resource).filter(models.Resource.id == resource_id).delete(synchronize_session=False); db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)