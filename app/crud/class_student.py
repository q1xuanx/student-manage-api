from asyncpg.connection import Connection
from asyncpg import Record
from typing import List, Optional
from ..schema.class_student import StudentClass, UpdateStudentClass

async def insert_new_class(conn : Connection, student_class : StudentClass) -> bool : 
    status = await conn.execute("INSERT INTO studentclass (classname) values ($1)", student_class.class_name)
    if status: 
        return True
    return False

async def update_class(conn : Connection, class_update : UpdateStudentClass) -> bool: 
    status = await conn.execute("UPDATE studentclass SET classname=$1 WHERE classid=$2", class_update.id, class_update.class_name)
    if status: 
        return True 
    return False

async def valid_class(conn : Connection, id_class : int) -> bool: 
    status = await conn.fetchval("SELECT classid FROM studentclass WHERE classid = $1", id_class)
    if status != None:
        return True
    return False

async def list_class (conn: Connection, limit : int, skip: int) -> List[Record]: 
    list_class = await conn.fetch("SELECT * FROM studentclass LIMIT $1 OFFSET $2", limit, skip)
    return list_class

async def total_item (conn: Connection) -> int: 
    return await conn.fetchval("SELECT COUNT(*) FROM studentclass")

async def check_valid_class_name(conn : Connection, class_name : str) -> Optional[Record]: 
    return await conn.fetchrow("SELECT classname from studentclass where classname ILIKE $1", class_name)

async def search_student_by_class(conn : Connection, class_search : str) -> List[Record]: 
    return await conn.fetch("select idstudent, s.namestudent, dob, sc.classname, faculty from students as s join studentclass as sc on s.classid = sc.classid where sc.classname ILIKE $1 group by sc.classname, s.namestudent, idstudent, dob, faculty order by sc.classname", f"%{class_search}%")
