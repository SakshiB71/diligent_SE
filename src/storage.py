import json
from pathlib import Path
from typing import List

# Path to the JSON file
DATA_FILE = Path("expenses.json")


def load_expenses() -> List[dict]:
    """
    Load all expenses from the JSON file.
    Returns an empty list if the file doesn't exist
    or is empty.
    """

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except json.JSONDecodeError:
        return []


def save_expenses(expenses: List[dict]) -> None:
    """
    Save all expenses to the JSON file.
    """

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            expenses,
            file,
            indent=4,
            ensure_ascii=False
        )