from ..schema.auth import AuthModel
from ..settings import setting
from ..schema.response import TokenResponse

def login(auth : AuthModel) -> TokenResponse: 
    username = setting.RAW_USERNAME
    password = setting.RAW_PASSWORD
    if auth.username == username and auth.password == password:
        return {
            'code': 200,
            'message': 'success',
            'token': setting.API_TOKEN
        } 
    return {
        'code': 400, 
        'message': 'Username or password incorrect',
        'token': ''
    }
    
