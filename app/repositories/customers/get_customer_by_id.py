from sqlmodel import Session, select
from ...models.model import Customer

class GetCustomerByIdRepository:
    @staticmethod
    def get(session: Session, customer_id: int):
        response = select(Customer).where(Customer.id == customer_id)

        customer = session.exec(response).first()

        return customer