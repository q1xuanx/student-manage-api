from asyncpg.connection import Connection
from ..schema.student import StudentModel, UpdateStudentModel
from datetime import date
from typing import Dict
from . import class_student


async def check_valid_id_class(conn : Connection, id_class : int) -> bool:
    status = await class_student.valid_class(conn, id_class)
    return status

async def add_student(conn : Connection, student : StudentModel) -> bool: 
    status = await conn.execute("INSERT INTO students(namestudent, dob, faculty, classid) values($1, $2, $3, $4)", student.name_student, student.dob, student.faculty, student.class_id)
    if status: 
        return True
    return False

async def update_student(conn : Connection, student : UpdateStudentModel) -> bool:
    status = await conn.execute("UPDATE students SET namestudent=$1, dob=$2, faculty=$3, classid=$4 WHERE idstudent=$5", student.name_student, student.dob, student.faculty, student.class_id, student.id)
    if status: 
        return True
    return False

async def delete_student(conn : Connection, id_student : int) -> bool: 
    status = await conn.execute("DELETE FROM students WHERE idstudent=$1", id_student)
    if status: 
        return True
    return False


async def check_exist_student(conn : Connection, student : StudentModel) -> bool:
    status = await conn.fetchrow("SELECT idstudent FROM students WHERE namestudent ILIKE $1 AND dob = $2 AND faculty = $3", student.name_student, student.dob, student.faculty)
    if status == None:
        return False
    return True

async def search_student(limit : int, offset : int, conn : Connection, name_student : str | None = None, dob : date| None = None, faculty : str | None = None, class_id : int | None = None) -> Dict[str, any]: 
    base_query = "SELECT idstudent, namestudent, faculty, s.classid, dob FROM students as s LEFT JOIN studentclass as sc ON s.classid=sc.classid WHERE 1=1"
    params = []
    if name_student: 
        base_query += f" AND namestudent LIKE ${len(params) + 1}"
        params.append(f"{name_student}%")
    if dob: 
        base_query += f" AND dob = ${len(params) + 1}"
        params.append(dob) 
    if faculty: 
        base_query += f" AND faculty = ${len(params) + 1}"
        params.append(faculty)
    if class_id: 
        base_query += f" AND classid = ${len(params) + 1}"
        params.append(class_id)
    base_query += f' LIMIT {limit} OFFSET {offset}'
    get_list_student = await conn.fetch(base_query, *params)
    if not get_list_student:
        return {
            'status': False
        }
    list_student = []
    for student in get_list_student:
        stu = UpdateStudentModel(id=student['idstudent'], 
                                 name_student=student['namestudent'],
                                 dob=student['dob'], 
                                 faculty=student['faculty'], 
                                 class_id=student['classid'])
        list_student.append(stu)
    get_total_query = base_query.replace('SELECT idstudent, namestudent, faculty, s.classid, dob ', 'SELECT COUNT(*) ')
    get_total_query = get_total_query.replace(f'LIMIT {limit} OFFSET {offset}', '')
    totals = await conn.fetchval(get_total_query, *params)
    total_student = totals
    return {
        'status': True,
        'list': list_student, 
        'total': total_student
    }



