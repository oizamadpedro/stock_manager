from pydantic import BaseModel

class ProductService: # make integration in db and the logic here
    def get(): pass
    
    def create(): pass # needs category

    def update(): pass

    def delete(): pass

    def find_one(): pass

class ProductModel(BaseModel): # make models
    name: str
    description: str
    price: float
    category_id: int
    quantity: int
    expiration_date: str
    created_at: str
    updated_at: str