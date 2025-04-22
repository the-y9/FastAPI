# main.py
from fastapi import FastAPI
from backend.api.auth import router as auth_router 

app = FastAPI()

@app.get('/')
def root():
    return {"page":"Root"}

app.include_router(auth_router)

