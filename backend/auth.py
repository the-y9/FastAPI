# auth.py
from .models import UserLogin


def handle_user_login(user: UserLogin):
    # Extract the username and password from the user model
    username = user.username
    password = user.password
    
    # Simple login logic (for example purposes)
    print(f"User: {username}")
    return f"Hi, {username}, your password is: {password}"

# def user_signup(user: UserLogin):
