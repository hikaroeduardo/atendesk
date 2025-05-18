from sqlmodel import select, Session
from ...models.model import User

class GetUerByUsernameRepository:
    @staticmethod
    def get(session: Session, username: str):
        with session:
            response = select(User).where(User.username == username)

            user = session.exec(response).first()

            return user