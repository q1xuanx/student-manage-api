from asyncpg.connection import Connection
from models.class_model import StudentClass, UpdateStudentClass

async def insert_new_class(conn : Connection, student_class : StudentClass): 
    status = await conn.execute("INSERT INTO studentclass (classname) values ($1)", student_class.class_name)
    if status: 
        return True
    return False

async def update_class(conn : Connection, class_update : UpdateStudentClass): 
    status = await conn.execute("UPDATE studentclass SET classname=$1 WHERE classid=$2", class_update.id, class_update.class_name)
    if status: 
        return True 
    return False

async def list_class (conn: Connection, limit : int, skip: int): 
    list_class = await conn.fetch("SELECT * FROM studentclass LIMIT $1 OFFSET $2", limit, skip)
    return list_class

async def total_item (conn: Connection): 
    return await conn.fetchrow("SELECT COUNT(*) FROM studentclass")

async def check_valid_class_name(conn : Connection, class_name : str): 
    return await conn.fetchrow("SELECT classname from studentclass where LOWER(classname) = LOWER($1)", class_name)