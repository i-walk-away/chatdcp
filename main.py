import uvicorn
from fastapi import FastAPI

from src.routes import messages, users, auth, chats

app = FastAPI(swagger_ui_parameters={"operationsSorter": "method"})

app.include_router(auth.router)
app.include_router(messages.router)
app.include_router(users.router)
app.include_router(chats.router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000)
