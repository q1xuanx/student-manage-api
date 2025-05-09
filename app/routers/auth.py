from fastapi import APIRouter, Depends
from ..services import auth_service
from ..schema.auth import AuthModel
from ..schema.response import TokenResponse
from app.dependencies import authen_app
from authx import AuthX

router = APIRouter(tags=['Auth'])

@router.post('/login')
def login(auth : AuthModel, authend : AuthX = Depends(authen_app)) -> TokenResponse:
    return auth_service.login(auth, authend)
