# main.py
from fastapi import FastAPI
from backend.auth import handle_user_login
from backend.models import UserLogin

app = FastAPI()

@app.post('/user-login')
async def user_login(user: UserLogin):
    # Call the handle_user_login function from auth.py
    result = handle_user_login(user)
    return {"message": result}


