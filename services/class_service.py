from repositories import class_repository
from asyncpg.connection import Connection
from models.class_model import StudentClass, UpdateStudentClass
import math

async def add_new_class(conn : Connection, student : StudentClass): 
    check_valid_name_class = await class_repository.check_valid_class_name(conn, student.class_name)
    print(check_valid_name_class)
    if check_valid_name_class != None: 
        return 'Name class exist !'
    added = await class_repository.insert_new_class(conn, student)
    return added

async def update_class(conn : Connection, update_class : UpdateStudentClass): 
    updated = await class_repository.update_class(conn, update_class)
    return updated

async def get_list_class (conn : Connection, limit : int, skip : int) : 
    get_total_item = await class_repository.total_item(conn)
    total_item = get_total_item[0]
    if limit < 0 or limit > total_item:
        return 'Limit must greater or equal than 0 | less than total pages'
    if skip < 1 or skip > math.ceil(total_item / limit): 
        return 'Skip number must greater or equal than 0 | less than total pages'
    list_class = await class_repository.list_class(conn, limit, (skip - 1) * limit)
    return {
        'list': list_class,
        'total_page': math.floor(total_item / limit)
    }