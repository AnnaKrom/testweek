from sqlalchemy.orm import Session
from models import Product, ProductCategory
from schemas import ProductCreate, ProductCategoryCreate

# Категории
def get_category(db: Session, category_id: int):
    return db.query(ProductCategory).filter(ProductCategory.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ProductCategory).offset(skip).limit(limit).all()

def create_category(db: Session, category: ProductCategoryCreate):
    new_category = ProductCategory(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

# Товары
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product