from ..crud import student
from asyncpg.connection import Connection
from ..schema.student import StudentModel, UpdateStudentModel
from datetime import date
from ..schema.response import BaseResponse, DataResponse


async def add_student(conn : Connection, student : StudentModel) -> BaseResponse:
    check_exist = await student.check_exist_student(conn, student)
    if check_exist:
        return { 
                'code': 400,
                'message': 'Student Exist !'
            }
    
    status = await student.add_student(conn, student)
    if status: 
        return {
            'code': 200, 
            'message': 'Add success'
        }
    
    return { 
        'code': 400,
        'message': 'Add Fail !'
    }
    
async def update_student(conn : Connection, student : UpdateStudentModel) -> BaseResponse: 
    status = await student.update_student(conn, student)
    if status: 
            return { 
            'code': 200, 
            'message': 'Update success'
        }
    return {
        'code': 400, 
        'message': 'Update Failed'
    }
async def delete_student(conn : Connection, id_student : int) -> BaseResponse: 
    status = await student.delete_student(conn, id_student)
    if status: 
        return { 
            'code': 200, 
            'message': 'Delete success'
        }
    return {
        'code': 400, 
        'message': 'Delete Failed'
    }
async def search_student(conn : Connection, name_student : str | None = None, dob : date | None = None, faculty : str | None = None, id_class : int | None = None) -> DataResponse: 
    list_student_response = await student.search_student(conn, name_student, dob, faculty, id_class)
    if list_student_response['status']:
        return {
            'code': 200,
            'message': 'success',
            'data': {
                        'list': list_student_response['list'],
                        'total': list_student_response['total'] 
                    }
        }
    return {
        'code': 400,
        'message': 'not found', 
        'data': []
    }
    





