from pydantic import BaseModel

class StudentClass(BaseModel): 
    class_name : str
    
class UpdateStudentClass(StudentClass):
    id : int