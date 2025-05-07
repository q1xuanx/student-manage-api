from fastapi import APIRouter, Depends
from app.dependencies import get_db_pool
from ..schema.class_student import StudentClass, UpdateStudentClass
from ..schema.response import BaseResponse, DataResponse
from asyncpg.connection import Connection
from ..services import class_service

router = APIRouter(tags=['Class'])

@router.get('/health-check', response_model=BaseResponse)
def health_check() -> BaseResponse:
    return {
        'code': 200, 
        'message': 'success'
    }

@router.post('/add', response_model=BaseResponse)
async def add_new_class(student_class : StudentClass, conn : Connection = Depends(get_db_pool)) -> BaseResponse:
    status = await class_service.add_new_class(conn, student_class)
    return status

@router.patch('/update', response_model=BaseResponse)
async def update_class(update_class : UpdateStudentClass, conn : Connection = Depends(get_db_pool)) -> BaseResponse:
    status = await class_service.update_class(conn, update_class)
    return status
@router.get('/classes', response_model=DataResponse)
async def list_class(limit : int = 1, page : int = 1, conn : Connection = Depends(get_db_pool)) -> DataResponse:
    list_class = await class_service.get_list_class(conn, limit, page)
    return list_class

@router.get('/search', response_model=DataResponse)
async def search_student_by_class(class_name : str, conn : Connection = Depends(get_db_pool)) -> DataResponse:
    list_class = await class_service.search_student_by_class(conn, class_name)
    return list_class