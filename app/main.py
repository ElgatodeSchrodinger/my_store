from turtle import title
from fastapi import FastAPI

from api import api

app = FastAPI(
    title="My Store",
    description="Simple Catalog System",
    version="0.0.1",
    contact={
        "name": "Javier Quintana",
        "email": "javier.taipe.1998@gmail.com",
    },
)


@app.get("/status")
def health():
    return {"message": "Successful"}


app.include_router(api.api_router)
