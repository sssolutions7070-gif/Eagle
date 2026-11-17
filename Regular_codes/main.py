from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()


@app.get("/")
def get():
    return{"message":"Welcome TO Vision "}





