from pydantic import BaseModel, Field

class DataCreateUser(BaseModel):
    name: str = Field(max_length=50)
    email: str
    username: str = Field(max_length=20)
    password: str