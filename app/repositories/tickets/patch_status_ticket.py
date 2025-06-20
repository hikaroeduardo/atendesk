from sqlmodel import Session
from ...models.model import Ticket

class PatchStatusRepository:
    @staticmethod
    def patch(session: Session, ticket: Ticket, status: str):
        ticket.status = status
        session.add(ticket)
        session.commit()