from sqlmodel import select , func , desc
from Rag_reflex.model.Conversation_Model import Conversation, QAPair

max_exchange = 20 

def get_create_conversation(session)-> Conversation:
    """
    Core logic — decides whether to reuse the current conversation
    or start a fresh one.

    Flow:
        1. Fetch the most recent Conversation from the DB.
        2. Count how many QAPairs it already has.
        3. If 0 conversations exist OR the latest is full (>= 20 pairs)
        → create a new Conversation.
        4. Otherwise → return the existing one.
    """
    #1 fetching the most recent conv
    latest_conv = session.exec(
        select(Conversation).order_by(Conversation.id.desc())
    ).first()

    if latest_conv is None :
        return _create_new_conv(session)
    
    # count how many pairs 
    pair_count = session.exec(
        select(func.count(QAPair.id)).where(
            QAPair.Conversation_id == latest_conv.id
        )
    ).one()

    # if the conversation is full 
    if pair_count >= max_exchange:
        return _create_new_conv(session)
    
    # if the conv is not full 
    return latest_conv

def _create_new_conv(session) -> Conversation:
    new_conversation = Conversation()
    session.add(new_conversation)
    session.commit()
    session.refresh(new_conversation)
    return new_conversation  


def save_QAPair(session, question: str, answer: str) -> QAPair:
        """
    High-level function called after every RAG response.

    Steps:
        1. Resolve the correct conversation (new or existing).
        2. Create and save the QAPair linked to that conversation.
        3. Return the saved pair (useful for the frontend state).
        """
        Conversation = get_create_conversation(session)
        pair = QAPair(
            Conversation_id=Conversation.id,
            question=question,
            answer=answer
        )
        session.add(pair)
        session.commit()
        session.refresh(pair)

        return pair


    





