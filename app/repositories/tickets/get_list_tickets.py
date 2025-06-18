from sqlmodel import Session, select
from ...models.model import Ticket, Customer

class ListTicketsRepository:
    @staticmethod
    def list(session: Session, user_id: int, status: str):
        query = select(Ticket, Customer).where(Ticket.user_id == user_id, Ticket.status == status).join(Ticket.customer)

        responses = session.exec(query).fetchall()

        tickets = []

        for ticket in responses:
            data = {
                "ticket": {
                    "name": ticket[0].name,
                    "status": ticket[0].status,
                    "description": ticket[0].description,
                },
                "customer": {
                    "name": ticket[1].name,
                    "email": ticket[1].email,
                    "phone": ticket[1].phone
                }
            }

            tickets.append(data)

        
        return tickets