print("Welcome Todo App..")

from pymongo import MongoClient
from fastapi import FastAPI

app = FastAPI()

connection=MongoClient("mongodb+srv://atifahmedshaikh:atifahmed19@cluster0.malln0y.mongodb.net/expense?retryWrites=true&w=majority&appName=Cluster0")
db = connection["todo_db"]
todos_collection = db["todos"]

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



@app.get("/todos/")
def read_todos():
    todos = list(todos_collection.find())
    return todos