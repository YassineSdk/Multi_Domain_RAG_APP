import reflex as rx 
from Rag_reflex.model.FileModel import FileModel

class FileState(rx.State):
    doc_name : str = "" 
    details  : str = ""
    files: list[dict] = []

    def set_doc_name(self,value):
        self.doc_name = value

    def set_details(self,value):
        self.details = value

    def load_files(self):
        with rx.session() as session:
            results = session.exec(FileModel.select()).all()
            self.files = [{
                "title":f.title,
                "details":f.details }
                for f in results ]

    async def handle_upload(self,files: list[rx.UploadFile]):
        for file in files:
            with rx.session() as session:
                session.add(FileModel(
                    title=self.doc_name or file.filename,
                    details=self.details or "No details",
                    filename=file.filename ,
                ))

                session.commit()
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
        return rx.toast.success('File aploaded successfully !')
