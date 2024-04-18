print("Welcome Todo App..")

from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
try:
    connection = MongoClient("")
    db = connection["todo_db"]
    todos_collection = db["todos"]
    print("Connected to MongoDB")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

@app.get("/")
def read_root():
    return {"message": "Welcome to my Todo App server with python "}


@app.get("/items/{item_id}")
def read_item(item_id, q= None):
    return {"item_id": item_id, "q": q}
  
  
class Todo(BaseModel):
    title: str
    status:bool


@app.get("/users")
def read_users():
  users_list=["Atif","Ahmed","Shaikh"]
  print("I am from users route ")
  return {"users":users_list}



@app.get("/todos")
def read_todos():
  my_list=todos_collection.find({});
    # todos = list(todos_collection.find({}))
  print(type(my_list))
  return {"message":"Check console"}
  
  
@app.get("/my-todos")
def my_read_todos():
    my_cursor = todos_collection.find({})
    todos_list = list(my_cursor)

    for todo in todos_list:
        todo["_id"] = str(todo["_id"])
    
    print(type(todos_list))
    return {"todos": todos_list}



@app.post("/create-todo/")
def create_todo(todo: Todo):
    todo_dict = todo.dict()
    inserted_todo = todos_collection.insert_one(todo_dict)

    documentId = str(inserted_todo.inserted_id)
    print(f"Created Todo Documnet ID: {documentId}")

    return {"message":"Todo Created successfully"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: str, todo: Todo):
    todo_dict = todo.dict()
    updated_todo = todos_collection.update_one({"_id": todo_id}, {"$set": todo_dict})
    if updated_todo.modified_count == 0:
        # raise HTTPException(status_code=404, detail="TODO not found")
        return {"message": "TODO updated"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    deleted_todo = todos_collection.delete_one({"_id": todo_id})
    if deleted_todo.deleted_count == 0:
        # raise HTTPException(status_code=404, detail="TODO not found")
       return {"message": "TODO deleted"}

