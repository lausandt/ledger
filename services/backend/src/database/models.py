from datetime import date
from decimal import Decimal

from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(
        max_length=50, unique=True, description="needs to be email"
    )
    full_name = fields.CharField(max_length=50, null=False)
    password = fields.CharField(max_length=128, null=False)
    superuser = fields.BooleanField(default=False)
    active = fields.BooleanField(default=True)


class Period(models.Model):
    id = fields.IntField(pk=True)
    nr = fields.IntField(pk=False)
    start_date: date = fields.DateField()
    end_date: date = fields.DateField()


class Entry(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225)
    amount: Decimal = fields.DecimalField(max_digits=10, decimal_places=2)
    supplier = fields.CharField(max_length=225)
    content = fields.TextField()
    regular = fields.BooleanField
    period: Period = fields.ForeignKeyField("models.Period", related_name="entry")
    author: User = fields.ForeignKeyField("models.User", related_name="entry")
    created_at: date = fields.DateField()

    def __str__(self) -> str:
        return f"{self.title} {self.author.id} {self.created_at}"


class Budget(models.Model):
    id = fields.IntField(pk=True)
    amount: Decimal = fields.DecimalField(max_digits=10, decimal_places=2)
    created_at: date = fields.DateField()
    author: User = fields.ForeignKeyField("models.User", related_name="budget")
    period: Period = fields.ForeignKeyField("models.Period", related_name="period")
