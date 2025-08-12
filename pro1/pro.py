from fastapi import FastAPI, APIRouter, HTTPException
from database import get_collections

#  """for database saving permanent"""
from pydantic import BaseModel

app = FastAPI()
student_collection = get_collections()


# for dschema createng
class Student(BaseModel):
    name: str
    age: int
    grade: str
    hight: float


@app.get("/")
async def home():
    return list(student_collection.find({}, {"_id": 0}))


@app.post("/")
async def create(new: Student):
    try:
        res = student_collection.insert_one(dict(new))
        return {"status_code": 200, "id": str(res.inserted_id)}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"some error {e}")


@app.put("/students/{name}")
async def update_student(name: str, updated: Student):
    result = student_collection.update_one({"name": name}, {"$set": dict(updated)})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"msg": "Student updateed successfully"}


@app.delete("/students/{name}")
async def delete_student(name: str):
    result = student_collection.delete_one({"name": name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="student noot foundd")
    return {"msg": "student delleted"}


if __name__ == "__main__":

    import uvicorn

    uvicorn.run("pro:app", host="0.0.0.0", port=8000, reload=True)
