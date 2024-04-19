print("Welcome to Todo App with user Authentication in python !");

from fastapi import FastAPI
from pymongo import MongoClient

app=FastAPI();

def connect_mongoDB():
  try:
        client=MongoClient("")
        database = client["todo_with_auth"]
        user_collection = database["user"]
        todo_collection = database["todo"]
        print("MongoDB connected successfully !")
  except Exception as error:
    print("MongoDB connection failed !")


connect_mongoDB()


@app.get("/")
def index_route():
  return {"message":"Welcome to Index route of App "}




