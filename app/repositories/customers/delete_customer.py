from sqlmodel import Session
from ...models.model import Customer

class DeleteCustomerRepository:
    @staticmethod
    def delete(session: Session, customer: Customer):
        session.delete(customer)
        session.commit()