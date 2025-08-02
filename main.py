import uvicorn
from fastapi import FastAPI

from src.routes import messages, users, auth

app = FastAPI()

app.include_router(messages.router)
app.include_router(users.router)
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000)
