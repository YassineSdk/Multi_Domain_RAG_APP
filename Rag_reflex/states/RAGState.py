import reflex as rx 
from Rag_reflex.model.Conversation_Model import Conversation, QAPair
from sqlmodel import select 
from Rag_reflex.utils.llm_respond import llm_response
from Rag_reflex.utils.conversation_manager import get_create_conversation,save_QAPair 
from Rag_reflex.states.QAPairItem import QAPairItem 
import asyncio

class RAGState(rx.State):
    question: str = ""
    answer: str = ""
    current_pairs: list[QAPairItem] = []
    is_loading :bool = False 

    async def handle_question(self):
            """
            Called when the user submits a question.

            Flow:
                1. Set loading state.
                2. Call your RAG pipeline to get the answer.
                3. Save the Q&A pair via conversation_manager (20-exchange rule applied here).
                4. Refresh the displayed pairs.
                5. Clear the input.
            """
            if not self.question.strip():
                return 
            self.is_loading = True 
            yield 
            rag_answer = await asyncio.to_thread(llm_response, self.question)

            with rx.session() as session:
                save_QAPair(
                    session=session,
                    question=self.question,
                    answer=rag_answer
                )
            await self._load_current_pairs()

            self.answer = rag_answer 
            self.question = ""
            self.is_loading = False 

    async def _load_current_pairs(self):
        with rx.session() as session:
            latest = session.exec(
                select(Conversation).order_by(Conversation.id.desc())
            ).first()

            if latest is None:
                self.current_pairs = []
                return 
            pairs = session.exec(
                select(QAPair)
                .where(QAPair.Conversation_id == latest.id)
                .order_by(QAPair.created_at.asc())
            ).all()

            self.current_pairs = [
            QAPairItem(question=p.question, answer=p.answer)
            for p in pairs ]

    async def load_on_start(self):
        """
        Call this on page load so the chat history
        is restored if the user refreshes the page.
        """
        await self._load_current_pairs()

