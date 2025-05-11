from ..crud import student as student_crud
from asyncpg.connection import Connection
from ..schema.student import StudentModel, UpdateStudentModel
from datetime import date
from ..schema.response import BaseResponse, DataResponse
import random

async def validate_data(conn : Connection, student : StudentModel) -> BaseResponse: 
    valid_id_class = await student_crud.check_valid_id_class(conn, student.class_id)
    if not valid_id_class:
        return {
            'code': 400,
            'message': 'Id class not found !'
        }
    check_exist = await student_crud.check_exist_student(conn, student)
    if check_exist:
        return { 
                'code': 400,
                'message': 'Student Exist !'
            }
    return {
        'code': 200,
        'message': 'Data valid'
    }

async def add_student(conn : Connection, student : StudentModel) -> BaseResponse:
    #valid_data = await validate_data(conn, student)
    # if valid_data['code'] == 400:
    #     return valid_data
    status = await student_crud.add_student(conn, student)
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
    valid_data = await validate_data(conn, student)
    if valid_data['code'] == 400:
        return valid_data
    status = await student_crud.update_student(conn, student)
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
    status = await student_crud.delete_student(conn, id_student)
    if status: 
        return { 
            'code': 200, 
            'message': 'Delete success'
        }
    return {
        'code': 400, 
        'message': 'Delete Failed'
    }
async def search_student(conn : Connection, limit : int, offset : int, name_student : str | None = None, dob : date | None = None, faculty : str | None = None, id_class : int | None = None) -> DataResponse: 
    list_student_response = await student_crud.search_student(limit, (offset - 1) * limit, conn, name_student, dob, faculty, id_class)
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
    





