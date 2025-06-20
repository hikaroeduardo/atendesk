from pydantic import BaseModel

class UpdateTicketSchema(BaseModel):
    status: str