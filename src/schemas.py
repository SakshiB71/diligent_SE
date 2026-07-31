import datetime
from uuid import UUID
from pydantic import BaseModel, Field, field_validator


class ExpenseCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        description="Title of the expense",
        examples=["Lunch"],
    )

    amount: float = Field(
        ...,
        gt=0,
        description="Expense amount",
        examples=[12.50],
    )

    category: str = Field(
        ...,
        min_length=1,
        description="Expense category",
        examples=["Food"],
    )

    date: datetime.date = Field(
        ...,
        description="Date of the expense",
        examples=["2026-07-31"],
    )

    @field_validator("title", "category")
    @classmethod
    def validate_non_empty(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty or contain only spaces")

        return value


class Expense(ExpenseCreate):
    id: UUID


class TotalResponse(BaseModel):
    total: float = Field(
        ...,
        description="Overall expense total",
        examples=[250.75],
    )


class CategoryTotalResponse(BaseModel):
    category: str
    total: float = Field(
        ...,
        description="Total expense amount for a category",
        examples=[120.50],
    )