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
#@auth_req
async def add_student(request : Request, student : StudentModel) -> BaseResponse:
    status = await student_service.add_student(student)
    return status
