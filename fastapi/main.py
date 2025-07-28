from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
import uvicorn
import json
from fastapi import FastAPI, Request, Form
from pymongo import MongoClient
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
template_obj = Jinja2Templates(directory="templates")

conn = MongoClient("localhost", 27017)
# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     data_obj = {"name": "somansh","proprty":"hai"}
#     f"{data_obj}"
#     return templates.TemplateResponse(
#         request=request, name="index.html", context={'data': data_obj}
#     )
# def tem2():
#     l=[]
#     for i in range(11):
#         l.append(i)
#     return l

# @app.get("/")
# def read1s(request:Request):
   
#     # normal key and val; formate in con
#     context = {"header_items": request.headers, "request": request, }
 
#     return template_obj.TemplateResponse("index.html", context=context)



@app.get("/")
def redas(request:Request):
    context = { "request": request }
    return template_obj.TemplateResponse("test2.html", context=context)


@app.post("/")
async def dasd(request: Request):
    x = await request.body()
    body_data = json.loads(x)
    return template_obj.TemplateResponse("test2.html", context={"request": request, "form_data": body_data})


# @app.post("/")
# def dasd(request: Request, name: str = Form(...), email: str = Form(...)):
#     form_data = {"name": name, "email": email}
#     return template_obj.TemplateResponse("test2.html", context={"request": request, "form_data": form_data})


@app.get("/sec")
def re(request:Request):
    # data =conn.students.students.find({})
    # ndoc=[]
    # for doc in data:
        
    #     ndoc.append({
    #     "id ":doc["_id"],
    #     "note":doc["note"]
    #     })
    # context = { "request": request }
    return template_obj.TemplateResponse("test.html")



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)