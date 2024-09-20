from pydantic import (
    BaseModel,
    Field,
)


class Name(BaseModel):
    title: str
    first: str
    last: str


class Email(BaseModel):
    value: str = Field(alias='email')
