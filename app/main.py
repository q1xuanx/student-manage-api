from fastapi import FastAPI
from .routers import class_route, student_route, auth
from .utils.db import connect_db
from contextlib import asynccontextmanager
from authx import AuthX, AuthXConfig

config = AuthXConfig(
    JWT_ALGORITHM = 'HS256', 
    JWT_SECRET_KEY = 'SECRET_KEY', 
    JWT_TOKEN_LOCATION = ['headers']
)

authend_app = AuthX(config=config)

@asynccontextmanager
async def lifespan(app : FastAPI):
    app.state.db_pool = await connect_db.create_con()
    app.state.authen_app = authend_app
    print('Connect DB Success')
    yield
    await connect_db.close_con(app.state.db_pool)
    print('Close DB') 

app = FastAPI(lifespan=lifespan, title='Student Manage API')
authend_app.handle_errors(app)

app.include_router(student_route.router, prefix="/student")
app.include_router(class_route.router, prefix="/class")
app.include_router(auth.router, prefix='/auth')

