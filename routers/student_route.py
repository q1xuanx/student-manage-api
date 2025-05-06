from fastapi import APIRouter, Depends
from asyncpg.connection import Connection
from dependencies import get_db_pool
from services import student_service
from models.student_model import StudentModel, UpdateStudentModel
from datetime import date
router = APIRouter(tags=['Student'])

@router.get('/health-check')
def heath_check():
    return {
        'code': 200, 
        'message': 'Good'
    }

@router.post('/add-student')
async def add_student(student : StudentModel, conn : Connection = Depends(get_db_pool)):
    status = await student_service.add_student(conn, student)
    if status: 
        return {
            'code': 200, 
            'message': 'Add success'
        }
    return { 
        'code': 400,
        'message': 'Add failed'
    }

@router.patch('/update-student')
async def update_student(student : UpdateStudentModel, conn : Connection = Depends(get_db_pool)): 
    status = await student_service.update_student(conn, student)
    if status: 
        return { 
            'code': 200, 
            'message': 'Update success'
        }
    return {
        'code': 400, 
        'message': 'Update Failed'
    }

@router.delete('/delete-student/{id_student}')
async def delete_student(id_student : int, conn : Connection = Depends(get_db_pool)): 
    status = await student_service.delete_student(conn, id_student)
    if status: 
        return { 
            'code': 200, 
            'message': 'Delete success'
        }
    return {
        'code': 400, 
        'message': 'Delete Failed'
    }

@router.get('/search')
async def search_student(name_student : str | None = None, dob : date | None = None, faculty : str | None = None, id_class : int | None = None, conn : Connection = Depends(get_db_pool)): 
    list_student = await student_service.search_student(conn, name_student, dob, faculty, id_class)
    if type(list_student) == str: 
        return {
            'code': 400, 
            'message': list_student
        }
    return {
        'code': 200, 
        'message': 'Success', 
        'data': list_student
    }