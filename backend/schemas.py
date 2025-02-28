from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str  # "cliente" o "agricultor"

class UserLogin(BaseModel):
    email: EmailStr
    password: str
