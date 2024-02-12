'''
main : programme principal
'''
#~ from typing import Annotated
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

users=[{'user':'admin', 'pwd':'admin'}]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def read_test(request: Request, x:str = None):
    #~ print('x=', x)
    return templates.TemplateResponse(
        request=request, name="template1.html", context={"name": "Emmanuel", "x": x}
    )

@app.post("/post_form")
def post_form(request: Request):
    print(request.data)
    return {"formulaire": request.data}
