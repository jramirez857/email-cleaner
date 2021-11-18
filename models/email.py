from pydantic import BaseModel


class Email(BaseModel):
    id: str
    sender: str
