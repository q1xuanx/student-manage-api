from fastapi import FastAPI
from routers import class_route, student_route
from db import connect_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app : FastAPI):
    app.state.db_pool = await connect_db.create_con()
    print('Connect DB Success')
    yield
    await connect_db.close_con(app.state.db_pool)
    print('Close DB') 

app = FastAPI(lifespan=lifespan)

app.include_router(student_route.router, prefix="/student")
app.include_router(class_route.router, prefix="/class")

