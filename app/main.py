import os
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI() 


@app.get("/vaimoving")
def hello_world():
    return {"message": "VaiMoving"}


handler = Mangum(app)