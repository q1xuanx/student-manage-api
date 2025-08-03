from ..schema.auth import AuthModel
from ..settings import setting
from ..schema.response import TokenResponse
from authx import AuthX


def login(auth: AuthModel, authend: AuthX) -> TokenResponse:
    username = setting.RAW_USERNAME
    password = setting.RAW_PASSWORD
    if auth.username == username and auth.password == password:
        token = authend.create_access_token(uid=auth.username)
        return {"code": 200, "message": "success", "token": token}
    return {"code": 400, "message": "Username or password incorrect", "token": ""}
