import reflex as rx 
from pydantic import BaseModel 
from typing import Optional

class QAPairItem(BaseModel):
    id: Optional[int] = None
    question : str 
    answer: str