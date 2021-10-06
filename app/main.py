import os
from fastapi import FastAPI
from mangum import Mangum

stage = "dev"
openapi_prefix = f"/{stage}" if stage else "/"

app = FastAPI(title="VaiMoving-app",openapi_prefix=openapi_prefix) 


@app.get("/vaimoving")
def hello_world():
    return {"message": "VaiMoving"}


handler = Mangum(app)