from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from .controllers import sandwiches, resources, recipes, order_details


from .models import models, schemas
from .controllers import orders
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)

@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db, sandwich)

@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)

@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    obj = sandwiches.read_one(db, sandwich_id)
    if obj is None: raise HTTPException(status_code=404, detail="Not found")
    return obj

@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def update_one_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    if sandwiches.read_one(db, sandwich_id) is None: raise HTTPException(status_code=404, detail="Not found")
    return sandwiches.update(db, sandwich_id, sandwich)

@app.delete("/sandwiches/{sandwich_id}", tags=["Sandwiches"])
def delete_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    if sandwiches.read_one(db, sandwich_id) is None: raise HTTPException(status_code=404, detail="Not found")
    return sandwiches.delete(db, sandwich_id)

@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db, resource)

@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)

@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    obj = resources.read_one(db, resource_id)
    if obj is None: raise HTTPException(status_code=404, detail="Not found")
    return obj

@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def update_one_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    if resources.read_one(db, resource_id) is None: raise HTTPException(status_code=404, detail="Not found")
    return resources.update(db, resource_id, resource)

@app.delete("/resources/{resource_id}", tags=["Resources"])
def delete_one_resource(resource_id: int, db: Session = Depends(get_db)):
    if resources.read_one(db, resource_id) is None: raise HTTPException(status_code=404, detail="Not found")
    return resources.delete(db, resource_id)

@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db, recipe)

@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)

@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    obj = recipes.read_one(db, recipe_id)
    if obj is None: raise HTTPException(status_code=404, detail="Not found")
    return obj

@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_one_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    if recipes.read_one(db, recipe_id) is None: raise HTTPException(status_code=404, detail="Not found")
    return recipes.update(db, recipe_id, recipe)

@app.delete("/recipes/{recipe_id}", tags=["Recipes"])
def delete_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    if recipes.read_one(db, recipe_id) is None: raise HTTPException(status_code=404, detail="Not found")
    return recipes.delete(db, recipe_id)

@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def create_order_detail(od: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db, od)

@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["OrderDetails"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)

@app.get("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def read_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    obj = order_details.read_one(db, order_detail_id)
    if obj is None: raise HTTPException(status_code=404, detail="Not found")
    return obj

@app.put("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def update_one_order_detail(order_detail_id: int, od: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    if order_details.read_one(db, order_detail_id) is None: raise HTTPException(status_code=404, detail="Not found")
    return order_details.update(db, order_detail_id, od)

@app.delete("/order_details/{order_detail_id}", tags=["OrderDetails"])
def delete_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    if order_details.read_one(db, order_detail_id) is None: raise HTTPException(status_code=404, detail="Not found")
    return order_details.delete(db, order_detail_id)
