from fastapi import APIRouter
from ..services import auth_service
from ..schema.auth import AuthModel
from ..schema.response import TokenResponse

router = APIRouter(tags=['Auth'])

@router.post('/login')
def login(auth : AuthModel) -> TokenResponse:
    return auth_service.login(auth)
