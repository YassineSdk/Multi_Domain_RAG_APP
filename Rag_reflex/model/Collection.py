import reflex as rx 
from sqlmodel import Field
from typing import Optional 
from  datetime import datetime


class Collection(rx.Model, table=True):
    id: Optional[int] = Field(default=None,primary_key=True)
    qa_pair_id: int = Field(foreign_key="qapair.id")
    title: str 
    saved_at: datetime = Field(default_factory=datetime.utcnow())
