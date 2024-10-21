from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import crud, schemas

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Зависимость для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинты для категорий
@app.get("/categories/", response_model=list[schemas.ProductCategory])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip=skip, limit=limit)

@app.post("/categories/", response_model=schemas.ProductCategory)
def create_category(category: schemas.ProductCategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

# Эндпоинты для товаров
@app.get("/products/", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)
    