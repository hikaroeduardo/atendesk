from sqlmodel import Field, SQLModel, create_engine
from .models.model import User, Ticket, Customer

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


def create_all_tables():
    SQLModel.metadata.create_all(engine)