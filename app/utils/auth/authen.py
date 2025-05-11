from fastapi import Request, HTTPException
from functools import wraps
from typing import Callable
from authx import AuthX, RequestToken

def auth_req(func : Callable): 
    @wraps(func)
    async def wrapper(*args, **kwargs):
        req : Request = kwargs.get("request")
        if not req: 
            for arg in args: 
                if isinstance(arg, Request):
                    req = arg
                    break
        if not req:
            raise HTTPException(status_code=400, detail="Missing request")
        authx : AuthX = req.app.state.authen_app
        auth_header = req.headers.get("Authorization")
        if not auth_header: 
            raise HTTPException(status_code=401, detail='Token missing')
        try:
            token_str = auth_header[7:]
            request_token = RequestToken(token=token_str, location="headers")
            authx.verify_token(token=request_token)
        except Exception as e:
            raise HTTPException(401, detail={"message": str(e)}) from e
        return await func(*args, **kwargs)
    return wrapper