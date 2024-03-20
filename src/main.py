import uvicorn
from fastapi import FastAPI

from chat import chat_router

chat_app = FastAPI()
chat_app.include_router(chat_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
