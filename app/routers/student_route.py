from fastapi import APIRouter, Depends, Request
from asyncpg.connection import Connection
from app.dependencies import get_db_pool
from ..services import student_service
from ..schema.student import StudentModel, UpdateStudentModel
from ..schema.response import BaseResponse, DataResponse
from datetime import date
from ..utils.auth.authen import auth_req

router = APIRouter(tags=['Student'])

@router.get('/health-check', response_model=BaseResponse)
@auth_req
async def heath_check(request : Request) -> BaseResponse:
    return {
        'code': 200, 
        'message': 'Good'
    }

@router.post('/add-student', response_model=BaseResponse)
@auth_req
async def add_student(request : Request, student : StudentModel, conn : Connection = Depends(get_db_pool)) -> BaseResponse:
    status = await student_service.add_student(conn, student)
    return status

@router.patch('/update-student', response_model=BaseResponse)
@auth_req
async def update_student(request : Request, student : UpdateStudentModel, conn : Connection = Depends(get_db_pool)) -> BaseResponse: 
    status = await student_service.update_student(conn, student)
    return status

@router.delete('/delete-student/{id_student}', response_model=BaseResponse)
@auth_req
async def delete_student(request : Request, id_student : int, conn : Connection = Depends(get_db_pool)) -> BaseResponse: 
    status = await student_service.delete_student(conn, id_student)
    return status

@router.get('/search', response_model=DataResponse)
@auth_req
async def search_student(request : Request, name_student : str | None = None, dob : date | None = None, faculty : str | None = None, id_class : int | None = None, conn : Connection = Depends(get_db_pool)) -> DataResponse: 
    list_student = await student_service.search_student(conn, name_student, dob, faculty, id_class)
    return list_student