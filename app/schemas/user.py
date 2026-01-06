from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr

from app.core.security import hash_password

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: UUID
    email:EmailStr
    is_active: bool
    is_verified:bool
    is_superuser: bool
    created_at: datetime

    class Config:
        from_attributes = True