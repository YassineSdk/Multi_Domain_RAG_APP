import reflex as rx 
from Rag_reflex.model.FileModel import FileModel
import sqlmodel

class FileState(rx.State):
    doc_name : str = "" 
    details  : str = ""
    files: list[dict] = []
    checked_files: list[str] = []

    #handles file checking
    def handle_check(self,title: str, value: bool):
        if value :
            self.checked_files.append(title)
        else :
            self.checked_files.remove(title)
    def clear_cheked_files(self):
        self.checked_files = []


    #handles passting the name to the variable
    def set_doc_name(self,value):
        self.doc_name = value

    #handles passting the details to the variable
    def set_details(self,value):
        self.details = value

    #load the files and returns a dict of { title ; details}
    def load_files(self):
        with rx.session() as session:
            results = session.exec(FileModel.select()).all()
            self.files = [{
                "title":f.title,
                "details":f.details }
                for f in results ]

    # handles files deleting and refreshes the UI 
    def delete_files(self):
            with rx.session() as session:
                for title in self.checked_files :
                    file = session.exec(
                            sqlmodel.select(FileModel).where(FileModel.title == title)
                        ).first()
                    if file:
                            session.delete(file)
                            session.commit()
            # refreching the UI and cleaning the selected files 
            self.clear_cheked_files()
            self.load_files()
            return rx.toast.success('Files deleted successfully !',position="top-right")

    # appload the files metdata to the db and updates the UI
    async def handle_upload(self,files: list[rx.UploadFile]):
        for file in files:
            with rx.session() as session:
                session.add(FileModel(
                    title=self.doc_name or file.filename,
                    details=self.details or "No details",
                    filename=file.filename ,
                ))

                session.commit()
        # we refresh the UI when adding a new file        
        self.files.append(
            {
                "title": self.doc_name or file.filename,
                "details":self.details or "No details"

            }
        )
        
        #reset the fields
        self.doc_name = ""
        self.details = ""
        self.load_files()
        return rx.toast.success('File aploaded successfully !',position="top-right")

