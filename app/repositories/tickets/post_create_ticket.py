from sqlmodel import Session
from ...models.model import Ticket

class CreateTicketRepository:
    @staticmethod
    def create(session: Session, user_id: int, customer_id: int, name: str, description: str):
        status = "Aberto"

        ticket = Ticket(user_id=user_id, customer_id=customer_id, name=name, description=description, status=status)

        session.add(ticket)
        session.commit()