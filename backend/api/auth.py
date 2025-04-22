
from fastapi import APIRouter
from backend.services.auth_service import handle_user_login, handle_user_signup
from backend.models import UserLogin, UserSignup

router = APIRouter()

@router.post('/user-login')
async def user_login(user: UserLogin):
    try:
        res = await handle_user_login(user)
        return {"message": res}
    except Exception as e:
        return {"ERROR:": str(e)}

@router.post('/user-signup')
async def user_signup(user: UserSignup):
    try:
        res = await handle_user_signup(user)
        return {"response": res}
    except Exception as e:
        return {"ERROR:": str(e)}