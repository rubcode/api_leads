from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class LeadRequest(BaseModel):
    name: str
    email: EmailStr
    company: Optional[str] = None
    message: str

    @field_validator("name")
    def validate_name(cls, v):
        if len(v.strip()) < 3:
            raise ValueError("Nombre inválido")
        return v