from fastapi import FastAPI


app = FastAPI()

@app.get("/")  #route
def index():
    return {"data" : {"name": "Aman", "title": "kishor" }, "address" : "patna"}

@app.get("/about")
def about(): #function to handle the req 
    return {"hey this is about page"}