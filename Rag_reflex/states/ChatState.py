import reflex as rx 



class ChatState(rx.State):
    message: str = ""
    question: str = ""
    is_loading : bool = False 
    conv_id: str = ""

    def set_question(self, value: str):
        self.question = value 
    
    def on_load(self):
        """ Loads latest conversation on page load.
            - If it has < 20 messages (not ended) → load its messages
            - If it has 20 messages (ended) or no conv exists → start blank conv
        """
        with rx.session() as session:
            latest_conv = session.exex(
                select(Conversation)
                .order_by(desc(Conversation.created_at))
                .limit(1)
            ).first()
        
        if latest_conv:
            messages = session.exec(
                select(QAPair)
                .where(QAPair.conv_id == latest_conv.id)
                .order_by(QAPair.created_at)
            ).all()

            if len(messages) < 20:
                self.conv_id = latest_conv.id 
                self.message = 
