from pydantic import BaseModel


class Email(BaseModel):
    id: str
    size: int
    sender: str
    subject: str
