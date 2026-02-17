import reflex as rx 



class FileModel(rx.Model,table=True):
    title: str 
    details:str
    filename: str 



