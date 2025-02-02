from pydantic import BaseModel
from typing import Optional

# Make a base class for the student
class NewStudents(BaseModel):
    name:str
    age:int
    Roll:int


class UpdateStudents(BaseModel):
    name:Optional[str]
    age:Optional[int]
    Roll:Optional[int]
