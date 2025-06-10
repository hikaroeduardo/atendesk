from sqlmodel import Session

from ...models.model import Customer

class CreateCustomerRepository:
    @staticmethod
    def create(session: Session, name: str, phone: str, email: str, user_id: int):
        with session:
            customer = Customer(name=name, phone=phone, email=email, user_id=user_id)

            session.add(customer)
            session.commit()