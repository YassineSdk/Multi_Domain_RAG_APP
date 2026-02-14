import reflex as rx 

class UploadState(rx.State):

    def upload_file(self):
        return rx.toast.success('Document uploaded!',duration=5000,position="top-right")