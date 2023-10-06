import typing
from datetime import datetime
from enum import IntEnum

from pydantic import BaseModel


class Categories(IntEnum):
    MYSTERY = 0
    SCIENCE_FICTION = 1
    SELF_HELP = 2


class BookSaveModel(BaseModel):
    id: typing.Optional[str] = None
    category: typing.Optional[Categories] = None
    title: typing.Optional[str] = None


class BookDBModel(BaseModel):
    id: str
    category: Categories
    title: str
    created_at: datetime
    updated_at: datetime
