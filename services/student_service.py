from repositories import student_repository
from asyncpg.connection import Connection
from models.student_model import StudentModel, UpdateStudentModel
from datetime import date

async def add_student(conn : Connection, student : StudentModel):
    return await student_repository.add_student(conn, student)
async def update_student(conn : Connection, student : UpdateStudentModel): 
    return await student_repository.update_student(conn, student)
async def delete_student(conn : Connection, id_student : int): 
    return await student_repository.delete_student(conn, id_student)
async def search_student(conn : Connection, name_student : str | None = None, dob : date | None = None, faculty : str | None = None, id_class : int | None = None): 
    return await student_repository.search_student(conn, name_student, dob, faculty, id_class)
    





