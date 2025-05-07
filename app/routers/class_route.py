from fastapi import APIRouter, Depends, Request
from app.dependencies import get_db_pool
from ..schema.class_student import StudentClass, UpdateStudentClass
from ..schema.response import BaseResponse, DataResponse
from asyncpg.connection import Connection
from ..services import class_service
from ..utils.auth.authen import auth_req

router = APIRouter(tags=['Class'])

@router.get('/health-check', response_model=BaseResponse)
@auth_req
async def health_check(request : Request) -> BaseResponse:
    return {
        'code': 200, 
        'message': 'success'
    }

@router.post('/add', response_model=BaseResponse)
@auth_req
async def add_new_class(request : Request, student_class : StudentClass, conn : Connection = Depends(get_db_pool)) -> BaseResponse:
    status = await class_service.add_new_class(conn, student_class)
    return status

@router.patch('/update', response_model=BaseResponse)
@auth_req
async def update_class(request : Request, update_class : UpdateStudentClass, conn : Connection = Depends(get_db_pool)) -> BaseResponse:
    status = await class_service.update_class(conn, update_class)
    return status
@router.get('/classes', response_model=DataResponse)
@auth_req
async def list_class(request : Request, limit : int = 1, page : int = 1, conn : Connection = Depends(get_db_pool)) -> DataResponse:
    list_class = await class_service.get_list_class(conn, limit, page)
    return list_class

@router.get('/search', response_model=DataResponse)
@auth_req
async def search_student_by_class(request : Request, class_name : str, conn : Connection = Depends(get_db_pool)) -> DataResponse:
    list_class = await class_service.search_student_by_class(conn, class_name)
    return list_class