from asyncpg.connection import Connection
from models.student_model import StudentModel, UpdateStudentModel
from datetime import date
async def add_student(conn : Connection, student : StudentModel): 
    status = await conn.execute("INSERT INTO students(namestudent, dob, faculty, classid) values($1, $2, $3, $4)", student.name_student, student.dob, student.faculty, student.class_id)
    if status: 
        return True
    return False

async def update_student(conn : Connection, student : UpdateStudentModel):
    status = await conn.execute("UPDATE students SET namestudent=$1, dob=$2, faculty=$3, classid=$4 WHERE idstudent=$5", student.name_student, student.dob, student.faculty, student.class_id, student.id)
    if status: 
        return True
    return False

async def delete_student(conn : Connection, id_student : int): 
    status = await conn.execute("DELETE FROM students WHERE idstudent=$1", id_student)
    if status: 
        return True
    return False

async def search_student(conn : Connection, name_student : str | None = None, dob : date| None = None, faculty : str | None = None, class_id : int | None = None): 
    base_query = "SELECT *, COUNT(*) OVER() as TotalStudent FROM students WHERE 1=1 "
    params = []
    if name_student: 
        base_query += f" AND namestudent ILIKE ${len(params) + 1}"
        params.append(name_student)
    if dob: 
        base_query += f" AND dob = ${len(params) + 1}"
        params.append(dob) 
    if faculty: 
        base_query += f" AND faculty = ${len(params) + 1}"
        params.append(faculty)
    if class_id: 
        base_query += f" AND classid = ${len(params) + 1}"
        params.append(class_id)
    get_list_student = await conn.fetch(base_query, *params)
    if not get_list_student:
        return 'Not found !'
    list_student = []
    for student in get_list_student:
        stu = UpdateStudentModel(id=student['idstudent'], 
                                 name_student=student['namestudent'],
                                 dob=student['dob'], 
                                 faculty=student['faculty'], 
                                 class_id=student['classid'])
        list_student.append(stu)

    total_student= get_list_student[0]['totalstudent']
        
    return {
        'list': list_student, 
        'total': total_student
    }