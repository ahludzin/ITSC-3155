from sqlalchemy.orm import Session
from fastapi import status, Response
from ..models import models, schemas

def create(db: Session, recipe: schemas.RecipeCreate):
    obj = models.Recipe(**recipe.model_dump()); db.add(obj); db.commit(); db.refresh(obj); return obj

def read_all(db: Session): return db.query(models.Recipe).all()

def read_one(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def update(db: Session, recipe_id: int, recipe: schemas.RecipeUpdate):
    q = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    q.update(recipe.model_dump(exclude_unset=True), synchronize_session=False); db.commit(); return q.first()

def delete(db: Session, recipe_id: int):
    db.query(models.Recipe).filter(models.Recipe.id == recipe_id).delete(synchronize_session=False); db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)