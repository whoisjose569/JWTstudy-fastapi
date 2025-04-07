from pydantic import BaseModel
from typing import Optional


class UserModel(BaseModel):
    id: int
    email: str
    password: str
    role: Optional[str] = "default"
