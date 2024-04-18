print("Welcome Todo App..")

from pymongo import MongoClient
from fastapi import FastAPI

app = FastAPI()

connection=MongoClient("mongodb+srv://atifahmed19:my-pass@cluster0.ytfhno1.mongodb.net/my-database?retryWrites=true&w=majority")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id, q= None):
    return {"item_id": item_id, "q": q}
  
  
@app.get("/users")
def read_users():
  users_list=["Atif","Ahmed","Shaikh"]
  print("I am from users route ")
  return {"users":users_list}


