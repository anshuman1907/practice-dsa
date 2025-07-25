from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
import uvicorn
from pymongo import MongoClient
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
template_obj = Jinja2Templates(directory="templates")

# conn = MongoClient("mongodb://localhost:27017/")
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

@app.get("/")
def read1s(request:Request):
    # normal key and val; formate in con
    context = {"header_items": request.headers, "request": request, }
    return template_obj.TemplateResponse("index.html", context=context)




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)