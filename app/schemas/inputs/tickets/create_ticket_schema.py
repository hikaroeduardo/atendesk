from pydantic import BaseModel, Field

class DataCreateTicket(BaseModel):
    user_id: int
    customer_id: int
    name: str = Field(max_length=50)
    description: str