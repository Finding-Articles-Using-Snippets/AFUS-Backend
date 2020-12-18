from pydantic import BaseModel

class Search(BaseModel):
    user_id: str
    search: str