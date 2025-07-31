import uvicorn
from fastapi import FastAPI

from src.routes import messages

app = FastAPI()

app.include_router(messages.router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000)
