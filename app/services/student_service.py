import json
from ..crud import student as student_crud
from asyncpg.connection import Connection
from ..schema.student import StudentModel, UpdateStudentModel
from datetime import date
from ..schema.response import BaseResponse, DataResponse
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")


async def validate_data(conn: Connection, student: StudentModel) -> BaseResponse:
    valid_id_class = await student_crud.check_valid_id_class(conn, student.class_id)
    if not valid_id_class:
        return {"code": 400, "message": "Id class not found !"}
    check_exist = await student_crud.check_exist_student(conn, student)
    if check_exist:
        return {"code": 400, "message": "Student Exist !"}
    return {"code": 200, "message": "Data valid"}


async def add_student(student: StudentModel) -> BaseResponse:
    result = None

    msg = json.dumps(student.model_dump(mode="json")).encode("utf-8")
    try:
        future = producer.send("student", msg)
        result = future.get(timeout=5)
        print(f"===> Send success: {result}")
    except Exception as e:
        print(f"===> Error append when add student: {str(e)}")

    if result:
        return {"code": 200, "message": "Add success"}
    return {"code": 400, "message": "Add Fail !"}
