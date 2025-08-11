from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List

app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["product_db"]
collection = db["products"]

# Product schema
class Product(BaseModel):
    product_id: str
    product_name: str
    product_price: float

# Create Product
@app.post("/product")
def create_product(product: Product):
    if collection.find_one({"product_id": product.product_id}):
        raise HTTPException(status_code=400, detail="Product ID already exists")
    collection.insert_one(product.dict())
    return {"message": "Product added successfully"}

# Get All Products
@app.get("/products", response_model=List[Product])
def get_products():
    products = list(collection.find({}, {"_id": 0}))
    return products

# Get Product by ID
@app.get("/product/{product_id}", response_model=Product)
def get_product(product_id: str):
    product = collection.find_one({"product_id": product_id}, {"_id": 0})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Update Product
@app.put("/product/{product_id}")
def update_product(product_id: str, updated_product: Product):
    result = collection.update_one(
        {"product_id": product_id},
        {"$set": updated_product.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product updated successfully"}

# Delete Product
@app.delete("/product/{product_id}")
def delete_product(product_id: str):
    result = collection.delete_one({"product_id": product_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
