from fastapi import FastAPI
from pydantic import  BaseModel
from .Schemas import Blog , Blogs
from db.connect import connect_db


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await connect_db() 




@app.post("/create")
async def createBlog(blog:Blog):
    res = Blogs(title=blog.title, body = blog.body )
    await res.insert()
    return {"message" : "blog is created"}