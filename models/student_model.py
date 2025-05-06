from pydantic import BaseModel
from datetime import date

class StudentModel(BaseModel): 
    name_student : str
    dob : date
    faculty : str 
    class_id : int

class UpdateStudentModel(StudentModel): 
    id : int
