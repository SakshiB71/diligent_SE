from fastapi import APIRouter, HTTPException, Response, status

from src.schemas import (
    ExpenseCreate,
    Expense,
    TotalResponse,
    CategoryTotalResponse,
)

from src.services import (
    create_expense,
    get_all_expenses,
    get_expenses_by_category,
    calculate_total,
    calculate_category_total,
    delete_expense,
)

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"],
)


@router.post(
    "",
    response_model=Expense,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new expense",
    description="Adds a new expense and stores it in the local JSON file.",
)
def add_expense(expense: ExpenseCreate):
    """
    Create and store a new expense.
    """
    return create_expense(expense)


@router.get(
    "",
    response_model=list[Expense],
    summary="List expenses",
    description="Returns all expenses. Optionally filter results using the category query parameter.",
)
def list_expenses(category: str | None = None):
    """
    Return all expenses or filter them by category.
    """
    if category:
        return get_expenses_by_category(category)

    return get_all_expenses()


@router.get(
    "/total",
    response_model=TotalResponse,
    summary="Calculate overall expenses",
    description="Calculates the total amount of all recorded expenses.",
)
def get_total():
    """
    Return the total amount of all expenses.
    """
    return calculate_total()


@router.get(
    "/total/{category}",
    response_model=CategoryTotalResponse,
    summary="Calculate category total",
    description="Calculates the total amount spent in a specific category.",
)
def get_category_total(category: str):
    """
    Return the total for a specific expense category.
    """
    return calculate_category_total(category)


@router.delete(
    "/{expense_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an expense",
    description="Deletes an expense using its unique ID.",
)
def remove_expense(expense_id: str):
    """
    Delete an expense by its ID.
    """
    deleted = delete_expense(expense_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense with the given ID was not found.",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)