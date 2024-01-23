"""
Tortoise comes with a pydantic model creating function
which creates the pydantic models for you:
1 - UserInSchema for creating new users
2 - UserOutSchema, user objects for use outside the application
3 - UserDatabaseSchema, user object for use within the application for most for validation
"""

from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import User


UserInSchema = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)

UserOutSchema = pydantic_model_creator(
    User, name="UserOut", exclude=["password", "active", "superuser"]
)

UserDatabaseSchema = pydantic_model_creator(User, name="User")
