from sqlmodel import select, Session
from ...models.model import Customer

class GetCustomerByEmailRepository:
    @staticmethod
    def get(session: Session, email: str):
        with session:
            response = select(Customer).where(Customer.email == email)

            customer = session.exec(response).first()

            return customer