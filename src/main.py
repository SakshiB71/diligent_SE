from fastapi import FastAPI

from src.routes import router

app = FastAPI(
    title="Smart Expense Tracker API",
    description="""
A REST API for managing personal expenses.

## Features

- Add new expenses
- View all recorded expenses
- Filter expenses by category
- Calculate overall expenses
- Calculate category-wise expense totals
- Delete expenses

Data is stored in a local JSON file, allowing expenses to persist between server restarts without requiring a database.
""",
    version="1.0.0",
    contact={
        "name": "Sakshi",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(router)


@app.get(
    "/",
    tags=["Home"],
    summary="API welcome message",
    description="Returns a welcome message confirming that the API is running.",
)
def root():
    """
    Return a simple welcome message.
    """
    return {
        "message": "Welcome to Smart Expense Tracker API"
    }