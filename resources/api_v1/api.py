from fastapi import APIRouter

from resources.api_v1.user import auth_router
from resources.api_v1.login import login_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix='/users', tags=['users'])
api_router.include_router(login_router, prefix='/login', tags=['login'])
