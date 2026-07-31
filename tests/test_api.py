import json
from pathlib import Path

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

DATA_FILE = Path("expenses.json")


def setup_function():
    """
    Reset the JSON file before every test.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump([], file)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Smart Expense Tracker API"
    }


def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31"
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Pizza"
    assert data["amount"] == 250
    assert data["category"] == "Food"
    assert "id" in data


def test_get_all_expenses():

    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31"
        },
    )

    response = client.get("/expenses")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == "Pizza"


def test_filter_by_category():

    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31"
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Uber",
            "amount": 300,
            "category": "Travel",
            "date": "2026-07-31"
        },
    )

    response = client.get("/expenses?category=Food")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["category"] == "Food"


def test_total_expenses():

    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31"
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Uber",
            "amount": 300,
            "category": "Travel",
            "date": "2026-07-31"
        },
    )

    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total"] == 550


def test_category_total():

    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31"
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Burger",
            "amount": 150,
            "category": "Food",
            "date": "2026-07-31"
        },
    )

    response = client.get("/expenses/total/Food")

    assert response.status_code == 200

    data = response.json()

    assert data["category"] == "Food"
    assert data["total"] == 400


def test_delete_expense():

    response = client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31"
        },
    )

    expense_id = response.json()["id"]

    delete_response = client.delete(f"/expenses/{expense_id}")

    assert delete_response.status_code == 204

    response = client.get("/expenses")

    assert len(response.json()) == 0


def test_delete_non_existing_expense():

    response = client.delete(
        "/expenses/12345678-1234-1234-1234-123456789012"
    )

    assert response.status_code == 404


def test_invalid_amount():

    response = client.post(
        "/expenses",
        json={
            "title": "Coffee",
            "amount": -50,
            "category": "Food",
            "date": "2026-07-31"
        },
    )

    assert response.status_code == 422