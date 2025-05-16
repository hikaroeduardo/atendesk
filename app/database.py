from sqlmodel import Field, SQLModel, create_engine, Session
from .models.model import User, Ticket, Customer

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

session = Session(engine)

def create_all_tables():
    SQLModel.metadata.create_all(engine)