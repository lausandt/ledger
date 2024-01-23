from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ..schemas.users import UserInSchema, UserOutSchema
from ..database.models import User
from ..crud import users
# from ..auth.jwthandler import get_current_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
# from ..auth.users import validate_user

router = APIRouter(
    prefix="/users",
    tags=["Users"],  # dependencies=[Depends(oauth2_scheme)]
)

@router.post("/register", response_model=UserOutSchema) 
async def create_user(user: UserInSchema):
    return await users.create_user(user)

# @router.post("/login")
# async def login(user: OAuth2PasswordRequestForm = Depends()):
#     user = await validate_user(user)

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     token = jsonable_encoder(access_token)
#     content = {"message": "You've successfully logged in. Welcome back!"}
#     response = JSONResponse(content=content)
#     response.set_cookie(
#         "Authorization",
#         value=f"Bearer {token}",
#         httponly=True,
#         max_age=1800,
#         expires=1800,
#         samesite="Lax",
#         secure=False,
#     )

#     return response


@router.get(
    "/",
    response_model=list[UserOutSchema], 
    # dependencies=[Depends(oauth2_scheme)],
)
async def get_users():
    return await users.get_users()


@router.get("/{username}", response_model=UserOutSchema) 
async def get_user(username: str):
    return await users.get_user(username)


@router.delete("/{user_id}")
async def delete_user(user_id: int ): #, current_user: User = Depends(get_current_user)):
    return await users.delete_user(user_id=user_id) #, current_user=current_user