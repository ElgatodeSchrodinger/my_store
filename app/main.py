from fastapi import FastAPI

from api import api

app = FastAPI()

@app.get("/status")
def health():
    return {
        "message": "Successful"
    }

app.include_router(api.api_router)