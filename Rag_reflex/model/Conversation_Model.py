import reflex as rx 
from typing import Optional, List
from datetime import datetime 
from sqlmodel import select , Field , Relationship


class Conversation(rx.Model, table=True):
    id: Optional[int] = Field(default=None,primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    pairs : List["QAPair"] = Relationship(back_populates="conversation")

class QAPair(rx.Model, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    Conversation_id: int = Field(foreign_key="conversation.id")
    question: str 
    answer: str 
    created_at: datetime = Field(default_factory=datetime.utcnow)
    conversation: Optional[Conversation] = Relationship(back_populates="pairs")







