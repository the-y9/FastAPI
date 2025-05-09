# models.py
from pydantic import BaseModel

# Define the UserLogin model
class UserLogin(BaseModel):
    username: str
    password: str

class UserSignup(BaseModel):
    username: str
    password: str
    email: str