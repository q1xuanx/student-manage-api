from pydantic import BaseModel
from datetime import date
from typing_extensions import List

class StudentModel(BaseModel): 
    name_student : str
    dob : date
    faculty : str 
    class_id : int

class UpdateStudentModel(StudentModel): 
    id : int

class DisplayStudentModel(BaseModel): 
    id_student : int 
    name_student : str
    dob : date
    class_name : str
    faculty : str

class GroupStudentModel(BaseModel): 
    students : List[DisplayStudentModel]
    totals : int