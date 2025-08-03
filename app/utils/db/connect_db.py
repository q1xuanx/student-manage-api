import asyncpg
import app.settings as st


class PostgreDB:
    _pool = None

    @classmethod
    async def create_con(cls):
        cls._pool = await asyncpg.create_pool(
            user=st.setting.POSTGRES_USER,
            password=st.setting.POSTGRES_PASSWORD,
            database=st.setting.POSTGRES_DB,
            host=st.setting.POSTGRES_SERVER,
            port=st.setting.POSTGRES_PORT,
            min_size=5,
            max_size=20,
        )
        return cls._pool

    @classmethod
    async def get_pool(cls):
        conn = await cls._pool.acquire()
        return conn

    @classmethod
    async def close_con(cls):
        await cls._pool.close()
