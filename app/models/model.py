from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    email: str
    username: str = Field(max_length=20)
    password: str

    tickets: list["Ticket"] = Relationship(back_populates="user")
    customers: list["Customer"] = Relationship(back_populates="user")

class Customer(SQLModel, table=True):
    __tablename__ = "customers"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    name: str = Field(max_length=50)
    phone: str = Field(max_length=15)
    email: str | None = Field(default=None, max_length=40)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    tickets: list["Ticket"] = Relationship(back_populates="customer")
    user: User = Relationship(back_populates="customers")

class Ticket(SQLModel, table=True):
    __tablename__ = "tickets"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    customer_id: int = Field(foreign_key="customers.id")
    name: str = Field(max_length=50)
    description: str
    status: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    customer: Customer = Relationship(back_populates="tickets")
    user: User = Relationship(back_populates="tickets")