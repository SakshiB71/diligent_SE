from uuid import uuid4

from src.logger import logger
from src.schemas import ExpenseCreate
from src.storage import load_expenses, save_expenses


def create_expense(expense: ExpenseCreate) -> dict:
    """
    Create a new expense, assign it a unique ID, and save it to storage.

    Args:
        expense: Validated expense data received from the API.

    Returns:
        dict: The newly created expense.
    """

    expenses = load_expenses()

    new_expense = {
        "id": str(uuid4()),
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
        "date": expense.date.isoformat(),
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    logger.info(f"Expense added: {expense.title}")

    return new_expense


def get_all_expenses() -> list[dict]:
    """
    Retrieve all stored expenses.

    Returns:
        list[dict]: A list containing every recorded expense.
    """

    logger.info("Fetching all expenses")

    return load_expenses()


def get_expenses_by_category(category: str) -> list[dict]:
    """
    Retrieve all expenses that belong to a specific category.

    Args:
        category: The category to filter by.

    Returns:
        list[dict]: Matching expenses for the requested category.
    """

    logger.info(f"Filtering expenses by category: {category}")

    expenses = load_expenses()

    return [
        expense
        for expense in expenses
        if expense["category"].lower() == category.lower()
    ]


def calculate_total() -> dict:
    """
    Calculate the sum of all recorded expenses.

    Returns:
        dict: A dictionary containing the overall total.
    """

    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    logger.info(f"Overall total calculated: {total}")

    return {"total": total}


def calculate_category_total(category: str) -> dict:
    """
    Calculate the total amount spent in a specific category.

    Args:
        category: The category to calculate the total for.

    Returns:
        dict: A dictionary containing the category name and total amount.
    """

    expenses = load_expenses()

    total = sum(
        expense["amount"]
        for expense in expenses
        if expense["category"].lower() == category.lower()
    )

    logger.info(f"{category} total calculated: {total}")

    return {
        "category": category,
        "total": total,
    }


def delete_expense(expense_id: str) -> bool:
    """
    Delete an expense using its unique ID.

    Args:
        expense_id: The unique identifier of the expense.

    Returns:
        bool: True if the expense was deleted, otherwise False.
    """

    expenses = load_expenses()

    updated_expenses = [
        expense
        for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        logger.warning(f"Expense not found: {expense_id}")
        return False

    save_expenses(updated_expenses)

    logger.info(f"Expense deleted: {expense_id}")

    return True