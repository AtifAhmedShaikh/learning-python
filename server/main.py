from fastapi import FastAPI
from pymongo import MongoClient
# from pydantic import BaseModel


app = FastAPI()
#mongodb+srv://atifahmed19:myJsCode19@cluster0.ytfhno1.mongodb.net/snapNewsData?retryWrites=true&w=majority 

# MongoDB Connection String
databaseConnectionURL = "mongodb+srv://atifahmed19:my-pass@cluster0.ytfhno1.mongodb.net/my-database?retryWrites=true&w=majority "

# # Connect to MongoDB
# client = MongoClient(databaseConnectionURL)
# db = client['my_python_database']
# collection = db['my_collection']
try:
  client = MongoClient(databaseConnectionURL)
  db = client['my_python_database']
  collection = db['my_collection']
  print("Database has Connected successfully ")
except Exception as error:
  print("Error while connecting database")  


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/test-route")
def test_route():
    obj={"message":"My Testing route is here !"}
    return obj

@app.get("/test-data")
def test_route():
    my_list = ["apple", "banana", "cherry"]
    obj = {"data": my_list, "message": "My Testing data route is here!"}
    return obj
  

@app.get("/test-params/{my_id}")
def test_params(my_id: str):
  print(my_id)
  return {"message":"Testing params"}

# class Todo(BaseModel):
#     name: str
#     age: int
#     email: str


# @app.get("/create-todo")
# def create_todo():