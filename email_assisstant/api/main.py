from fastapi import FastAPI
from api.routes import assistant

app = FastAPI()
app.include_router(assistant.router)

@app.get("/")
def root():
    return {"message": "AI Email Assistant is up and running!"}
