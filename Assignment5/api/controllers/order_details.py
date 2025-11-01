from sqlalchemy.orm import Session
from fastapi import status, Response
from ..models import models, schemas

def create(db: Session, od: schemas.OrderDetailCreate):
    obj = models.OrderDetail(**od.model_dump()); db.add(obj); db.commit(); db.refresh(obj); return obj

def read_all(db: Session): return db.query(models.OrderDetail).all()

def read_one(db: Session, order_detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

def update(db: Session, order_detail_id: int, od: schemas.OrderDetailUpdate):
    q = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    q.update(od.model_dump(exclude_unset=True), synchronize_session=False); db.commit(); return q.first()

def delete(db: Session, order_detail_id: int):
    db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).delete(synchronize_session=False); db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)