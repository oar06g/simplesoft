from pydantic import BaseModel, Field, EmailStr

class CreateUser(BaseModel):
    fullname: str = Field(...,min_length=4,max_length=75)
    age: int = Field(..., gt=18, lt=75)
    email: EmailStr = Field(...)
    password: str = Field(...)
    job_title: str = Field(...)
    years_of_experience: int = Field(...)