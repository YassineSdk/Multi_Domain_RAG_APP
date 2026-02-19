import reflex as rx 
from pydantic import BaseModel 

class QAPairItem(BaseModel):
    question : str 
    answer: str