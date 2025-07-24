from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
import uvicorn

app = FastAPI()

@app.get("/")
def dasdasdajsgdja(request: Request):
    print(request.headers)
    return {"message": "Hello, Worldadsdas!"}



@app.post("/")
def dasdasdajsgdja():
    return "This is a POST request."

def generic_function():
    return PlainTextResponse("This is a generic function.")


@app.get("/second")
def read_root():
    return generic_function()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)