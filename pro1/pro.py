from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():

    return {"massage": "Hedsfloo anshuman"}




if __name__ == '__main__':

    import uvicorn
    uvicorn.run('test:app', host="0.0.0.0", port=8000 ,reload= True)