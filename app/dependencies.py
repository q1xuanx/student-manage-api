from fastapi.requests import Request
from authx import AuthX

async def get_db_pool(request : Request):
    pool = request.app.state.db_pool
    async with pool.acquire() as conn: 
        yield conn

async def authen_app (request : Request) -> AuthX: 
    authen = request.app.state.authen_app
    yield authen