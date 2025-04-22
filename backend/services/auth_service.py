# auth.py
from ..models import UserLogin


async def handle_user_login(user: UserLogin):
    
    username = user.username
    password = user.password
    
    return f"Hi, {username}, your password is: {password}"

async def handle_user_signup(user: UserLogin):
    username = user.username
    password = user.password
    email = user.email
    
    return {"username": username, "email": email, "password": password}
