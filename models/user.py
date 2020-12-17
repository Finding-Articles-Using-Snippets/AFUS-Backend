from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    file_id: int
    search: str
