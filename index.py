from fastapi import FastAPI
from  typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/")  #route
def index():
    return {"data" : {"name": "Aman", "title": "kishor" }, "address" : "patna"}

@app.get("/about")
def about(): #path operation function to handle the req 
    return {"hey this is about page"}

@app.post("/post")
def post(name):
    return {f"post your name {name}"}


@app.get("/blogs/comments")
def hi():
    return {"all comments"}

@app.get("/blogs/{id}")
def show(id):
    return {'data': id}
 

class Blogs(BaseModel):
    name:str
    pages:int
    no_of_slides:str
    new : Optional[str] = None
    
@app.post("/blogs")
def create_blogs(blogs:Blogs):
    return blogs