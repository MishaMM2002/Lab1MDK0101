from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class Play(BaseModelModify):
    name: str
    type_id: int


class User(BaseModelModify):
    name: str
    phone: str
    password: Optional[str]
    post: str


class TypeOfPlay(BaseModelModify):
    name: str


class Hall(BaseModelModify):
    name: str
    number: int


class Ticket(BaseModelModify):
    performance_id: int
    user_id: int


class Performance(BaseModelModify):
    datetime_start: str
    play_id: int
    hall_id: int


class UserAuth(BaseModel):
    phone: str
    password: str

