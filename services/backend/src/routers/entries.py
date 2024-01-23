from fastapi import APIRouter
from src.schemas.entries import EntryInSchema, EntryOutSchema
from src.crud import entries

router = APIRouter(
    prefix="/entries",
    tags=["Entry"],  # dependencies=[Depends(oauth2_scheme)]
)

@router.post("/register", response_model=EntryOutSchema) 
async def create_entry(entry: EntryInSchema, user_id):
    return await entries.create_entry(entry, user_id)


@router.get(
    "/",
    response_model=list[EntryOutSchema], 
    # dependencies=[Depends(get_current_user)],
)
async def get_users():
    return await entries.get_entries()