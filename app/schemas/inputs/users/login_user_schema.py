from pydantic import BaseModel

class DataLoginUser(BaseModel):
    username: str
    password: str