from fastapi import FastAPI, APIRouter, HTTPException

# from database import get_collections
#  """for database saving permanent"""
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()


# mongo db for

client = MongoClient("mongodb://localhost:27017/")
db = client["product"]
collection = db["products"]


# for schemaa createng
class Product(BaseModel):
    product_id: int
    product_name: str
    product_price: float


# crud/
@app.post("/product")
async def create_product(Product: Product):
    if collection.find_one({"product_id": Product.product_id}):
        raise HTTPException(status_code=400, detail="product is already exisit")

    collection.insert_one(Product.dict())
    return {"massege": "product is succesfull added "}


@app.get("/products")
async def get_product():

    products = list(collection.find({}, {"_id": 0}))
    return products


@app.put("/product/{product_id}")
async def update_product(product_id :int,updated_product:Product):
    result = collection.update_one(  {"product_id":product_id},{"$set": updated_product.dict()})       
    
    if result.matched_count==0:
        raise HTTPException(status_code=404, detail="product is not found")
    
    return {"massege":"product is updated succesfully"}

@app.delete("/product/{product_id}")
def delete_product(product_id: int):
    result = collection.delete_one({"product_id": product_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="product is not found")

    return {"massge": "prioductis succesfu;;y delleted"}


if __name__ == "__main__":

    import uvicorn

    uvicorn.run("product:app", host="0.0.0.0", port=800, reload=True)
