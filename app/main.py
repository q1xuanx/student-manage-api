import asyncio
from fastapi import FastAPI
from app.routers import class_route, student_route, auth
from app.utils.db.connect_db import PostgreDB
from contextlib import asynccontextmanager
from authx import AuthX, AuthXConfig
from app.services.consumer import consum_student
import threading

config = AuthXConfig(
    JWT_ALGORITHM="HS256", JWT_SECRET_KEY="SECRET_KEY", JWT_TOKEN_LOCATION=["headers"]
)

authend_app = AuthX(config=config)


def run_stundent_consumer():
    asyncio.run(consum_student(), debug=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await PostgreDB.create_con()
    pool = await PostgreDB.get_pool()
    app.state.db_pool = pool
    app.state.authen_app = authend_app
    print("===> Connect DB Success")

    threading.Thread(target=run_stundent_consumer, daemon=True).start()
    # student_consumer_task = asyncio.create_task(consum_student())

    print("===> Kafka consumer already start")

    yield
    await PostgreDB.close_con(app.state.db_pool)
    print("===> Close DB")


app = FastAPI(lifespan=lifespan, title="Student Manage API")
authend_app.handle_errors(app)

app.include_router(student_route.router, prefix="/student")
app.include_router(class_route.router, prefix="/class")
app.include_router(auth.router, prefix="/auth")

# handler = Mangum(app, lifespan="auto")
