from fastapi import Request, HTTPException
from functools import wraps
from typing import Callable
from app.settings import setting

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
        
        token = req.headers.get("Authorization")
        #print(token)
        if token != setting.API_TOKEN: 
            raise HTTPException(status_code=403, detail='Invalid token')
        return await func(*args, **kwargs)
    return wrapper