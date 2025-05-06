from fastapi import APIRouter, Depends
from dependencies import get_db_pool
from models.class_model import StudentClass, UpdateStudentClass
from asyncpg.connection import Connection
from services import class_service

router = APIRouter(tags=['Class'])

@router.get('/health-check')
def health_check():
    return {
        'code': 200, 
        'message': 'success'
    }

@router.post('/add')
async def add_new_class(student_class : StudentClass, conn : Connection = Depends(get_db_pool)):
    status = await class_service.add_new_class(conn, student_class)
    if status and type(status) != str: 
        return {
            'code': 200,
            'message': 'add success'
        }
    return {
            'code': 404,
            'message': status
        }

@router.patch('/update')
async def update_class(update_class : UpdateStudentClass, conn : Connection = Depends(get_db_pool)):
    status = await class_service.update_class(conn, update_class)
    if status: 
        return {
            'code': 200,
            'message': 'update success'
        }
    return {
            'code': 404,
            'message': 'fail'
        }
@router.get('/classes')
async def list_class(limit : int = 1, page : int = 1, conn : Connection = Depends(get_db_pool)):
    list_class = await class_service.get_list_class(conn, limit, page)
    if type(list_class) == str: 
        return {
            'code': 400, 
            'message': list_class
        }
    return {
        'code' : 200, 
        'message': 'success', 
        'data': list_class
    }