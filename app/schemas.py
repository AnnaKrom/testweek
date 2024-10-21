from pydantic import BaseModel

class ProductCategoryBase(BaseModel):
    name: str
    description: str 

class ProductCategoryCreate(ProductCategoryBase):
    pass

class ProductCategory(ProductCategoryBase):
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    category_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True