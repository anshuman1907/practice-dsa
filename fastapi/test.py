from fastapi import FastAPI

app = FastAPI()

@app.get("/as")
async def home():

    return {"massage": "Hedsfloo anshuman"}
# @app.get("/products/{p_id}")
# async def read_item(p_id:int, sort):
#     return [p_id, sort]



# @app.post("/products/{p_id}")
# async def read_item(p_id:int, sort):
#     return [p_id, sort]




if __name__ == '__main__':

    import uvicorn
    uvicorn.run('test:app', host="0.0.0.0", port=8000 ,reload= True)