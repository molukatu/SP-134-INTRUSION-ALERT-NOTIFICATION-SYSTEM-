from pydantic import BaseModel
from typing import Optional

class Alert(BaseModel):
    id: int
    type: str
    severity: str
    src_ip: str
    status: str = "New"
    description: Optional[str] = None

class AlertCreate(BaseModel):
    type: str
    severity: str
    src_ip: str
    description: Optional[str] = None
