from fastapi import FastAPI
from routes.chat import router

app=FastAPI()

@app.get("/")
def home():
    return {
        "message" : "Ai Assistant Backend running"

    }


app.include_router(router)