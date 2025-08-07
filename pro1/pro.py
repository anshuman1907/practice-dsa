from fastapi import FastAPI
from database import get_collections

app = FastAPI()
student_collection = get_collections()

@app.get("/")
async def home():
    return list(student_collection.find({}, {"_id": 0}))




if __name__ == '__main__':

    import uvicorn
    uvicorn.run('pro:app', host="0.0.0.0", port=8000 ,reload= True)