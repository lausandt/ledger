"""
1 - EntryInSchema create new entries
2 - EntryOutSchema entry object for use outside of the application
3 - UpdateEntry schemas for updating existing entries
"""
from decimal import Decimal

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Entry


EntryInSchema = pydantic_model_creator(
    Entry, name="EntryIn", exclude=["author_id"], exclude_readonly=True
)
EntryOutSchema = pydantic_model_creator(
    Entry, name="Entry", exclude=["author.password", "author.superuser"]
)


class UpdateEntry(BaseModel):
    title: str | None
    content: str | None
    amount: Decimal | None
