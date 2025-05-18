from sqlmodel import Session

from ...models.model import User

class CreateUserRepository:
    @staticmethod
    def create(session: Session, username: str, password: str, email: str, name: str):
        with session:
            user = User(email=email, username=username, password=password, name=name)

            session.add(user)
            session.commit()