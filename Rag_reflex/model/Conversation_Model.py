import reflex as rx 
import uuid 
from datetime import datetime 
from sqlmodel import select , Field , desc 


# conversation db Model
class Conversation(rx.Model, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True),
    created_at : datetime = Field(default_factory=datetime.now)
    summary : str | None = Field(default=None)

# message db model 
class QAPair(rx.Model, table=True):
    id: int | None = Field(default=None,primary_key=True)
    conv_id: str 
    question: str 
    role : str
    answer: str | None = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now())


