from app.crud import class_student
from asyncpg.connection import Connection
from ..schema.class_student import StudentClass, UpdateStudentClass
from ..schema.student import DisplayStudentModel
import math
from typing import Dict, Any


async def add_new_class(conn: Connection, student: StudentClass) -> Dict[str, any]:
    check_valid_name_class = await class_student.check_valid_class_name(
        conn, student.class_name
    )
    if check_valid_name_class != None:
        return {"code": 400, "message": "Name class exist !"}
    status = await class_student.insert_new_class(conn, student)
    if status:
        return {"code": 200, "message": "Add Success"}
    return {"code": 400, "message": "Add fail"}


async def update_class(conn: Connection, update_class: UpdateStudentClass) -> bool:
    updated = await class_student.update_class(conn, update_class)
    return updated


async def get_list_class(conn: Connection, limit: int, skip: int) -> Dict[str, Any]:
    total_item = await class_student.total_item(conn)
    if limit < 0 or limit > total_item:
        return {
            "code": 400,
            "message": "Limit must greater or equal than 0 | less than total pages",
            "data": [],
        }
    if skip < 1 or skip > math.ceil(total_item / limit):
        return {
            "code": 400,
            "message": "Skip number must greater or equal than 0 | less than total pages",
            "data": [],
        }
    get_list_class = await class_student.list_class(conn, limit, (skip - 1) * limit)
    list_class = []
    for cl in get_list_class:
        clss = UpdateStudentClass(id=cl["classid"], class_name=cl["classname"])
        list_class.append(clss)
    return {
        "code": 200,
        "message": "success",
        "data": {"list": list_class, "total_page": math.floor(total_item / limit)},
    }


async def search_student_by_class(
    conn: Connection, class_search: str
) -> Dict[str, Any]:
    classes = await class_student.search_student_by_class(conn, class_search)
    list_class = {}
    for item in classes:
        student = DisplayStudentModel(
            id_student=item["idstudent"],
            name_student=item["namestudent"],
            dob=item["dob"],
            class_name=item["classname"],
            faculty=item["faculty"],
        )
        list_class.setdefault(item["classname"], {}).setdefault("students", []).append(
            student
        )
        list_class.setdefault(item["classname"], {}).setdefault("totals", 0)
        list_class[item["classname"]]["totals"] += 1
    return {"code": 200, "message": "success", "data": list_class}
