from fastapi import FastAPI
from pydantic import BaseModel

# Create the FastAPI instance
app = FastAPI()

# Define a data model using Pydantic
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# Define a simple GET endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define a POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price, "item_offer": item.is_offer}

# Define a GET endpoint with a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
