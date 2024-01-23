from src.database.models import Entry
from src.schemas.entries import EntryOutSchema, EntryInSchema


async def get_entries() -> list[EntryOutSchema]:
    return await EntryOutSchema.from_queryset(Entry.all())


async def create_entry(entry: EntryInSchema, user_id: int) -> EntryOutSchema:
    entry_dict = entry.dict(exclude_unset=True)
    entry_dict["author_id"] = user_id
    entry_obj = await Entry.create(**entry_dict)
    return await EntryOutSchema.from_tortoise_orm(entry_obj)
