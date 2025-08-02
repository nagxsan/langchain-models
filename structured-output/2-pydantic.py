from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'John Doe'
    age: Optional[int] = None
    email: Optional[EmailStr] = 'john@doe.com'
    cgpa: Optional[float] = Field(ge=0, le=10, default=6.9)

student = { 'name': 'Sanchet', 'age': 24, 'email': 'john@wick.com', 'cgpa': 10 }

basic_student = Student(**student)
print(basic_student)

default_student = Student(**{ 'age': 22 })
print(default_student)

optional_student = Student()
print(optional_student)
