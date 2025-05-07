import asyncpg
import asyncio
import app.settings as st

async def create_con(): 
    return await asyncpg.create_pool(
        user=st.setting.POSTGRES_USER, 
        password=st.setting.POSTGRES_PASSWORD, 
        database=st.setting.POSTGRES_DB, 
        host=st.setting.POSTGRES_SERVER,
        port=st.setting.POSTGRES_PORT
    )

async def close_con(pool):
    await pool.close()