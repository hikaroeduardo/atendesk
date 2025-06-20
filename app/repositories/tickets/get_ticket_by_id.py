from sqlmodel import Session, select
from ...models.model import Ticket

class GetTicketByIdRepository:
    @staticmethod
    def get(session: Session, id: int):
        query = select(Ticket).where(Ticket.id == id)

        response = session.exec(query).first()

        return response