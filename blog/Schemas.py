from pydantic import BaseModel
from beanie import Document
from typing import List , Literal


#input schema 
class Blog(BaseModel): 
    title:str
    body:str
    

#mongodb document model 
class Blogs(Document):
    title:str
    body:str
    