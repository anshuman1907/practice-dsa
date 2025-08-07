from fastapi import FastAPI,APIRouter, HTTPException
from database import get_collections
#  """for database saving permanent"""
from pydantic import BaseModel

app = FastAPI()
student_collection = get_collections()


class Student(BaseModel):
    name: str
    age: int
    grade: str


@app.get("/")
async def home():
    return list(student_collection.find({}, {"_id": 0}))



@app.post("/")
async def create(new:Student):
    try:
        res= student_collection.insert_one(dict(new))
        return {"status_code":200,"id":str(res.inserted_id)}
    
    except Exception as e:
        return HTTPException(status_code=500,detail=f"some error {e}")




if __name__ == '__main__':

    import uvicorn
    uvicorn.run('pro:app', host="0.0.0.0", port=8000 ,reload= True)