# Smart Expense Tracker API

A REST API for managing personal expenses built with FastAPI.

The API allows users to add, view, filter, summarize, and delete expenses while storing data in a local JSON file. The project focuses on clean code organization, request validation, and automated testing while keeping the implementation simple.

---

## Features

- Add a new expense
- View all recorded expenses
- Filter expenses by category
- Calculate the overall expense total
- Calculate totals for a specific category
- Delete an expense
- Validate incoming requests using Pydantic
- Interactive API documentation using Swagger UI
- Automated API tests using pytest

---

## Tech Stack

- Python 3.13
- FastAPI
- Pydantic
- Uvicorn
- pytest
- Local JSON file storage

---

## Project Structure

```text
diligent_SE/
│
├── src/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── routes.py        # API endpoints
│   ├── services.py      # Business logic
│   ├── storage.py       # JSON file operations
│   ├── schemas.py       # Request and response models
│   └── logger.py        # Logging configuration
│
├── tests/
│   └── test_api.py
│
├── expenses.json
├── requirements.txt
├── README.md
├── AI_NOTES.md
├── LICENSE
└── .gitignore
```

---

## Architecture

The application is divided into small layers so that each part has a single responsibility.

```text
Client
   │
   ▼
FastAPI Routes
   │
   ▼
Service Layer
   │
   ▼
Storage Layer
   │
   ▼
expenses.json
```

### Responsibilities

- **Routes** receive HTTP requests and return responses.
- **Services** contain the business logic.
- **Storage** reads from and writes to the JSON file.
- **Schemas** validate requests and define response models.

Keeping these responsibilities separate makes the project easier to understand, test, and maintain.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd diligent_SE
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the API

Start the development server:

```bash
uvicorn src.main:app --reload
```

Once the server is running, open:

```text
http://127.0.0.1:8000/docs
```

to access the automatically generated Swagger documentation.

---

## Running Tests

Run the automated test suite:

```bash
python -m pytest
```

The test suite covers the main API functionality, validation, and error handling.

---

## Validation

Incoming requests are validated using Pydantic before reaching the business logic.

Examples of invalid requests include:

- Empty title
- Empty category
- Negative or zero amount
- Invalid date format

Invalid requests return a **422 Unprocessable Entity** response.

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome endpoint |
| POST | `/expenses` | Add a new expense |
| GET | `/expenses` | View all expenses |
| GET | `/expenses?category=Food` | Filter expenses by category |
| GET | `/expenses/total` | Calculate the overall expense total |
| GET | `/expenses/total/{category}` | Calculate the total for a category |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

---

## Example Request

### Create Expense

**POST** `/expenses`

```json
{
  "title": "Lunch",
  "amount": 12.50,
  "category": "Food",
  "date": "2026-07-31"
}
```

Response (**201 Created**)

```json
{
  "id": "6d8d59a1-69fd-4b26-a2f1-59fc6c0bc7d2",
  "title": "Lunch",
  "amount": 12.5,
  "category": "Food",
  "date": "2026-07-31"
}
```

---

## Design Decisions

The assignment allowed storing data either in memory or in a local JSON file. I chose a JSON file because it keeps the implementation simple while allowing expenses to persist between server restarts.

Instead of placing all logic in a single file, I separated the application into routes, services, storage, and schemas. Each module has a single responsibility, which makes the code easier to read, test, and modify.

I chose FastAPI because it provides request validation through Pydantic and automatically generates Swagger documentation. This reduced boilerplate and allowed me to focus on the API design and business logic.

Automated tests were added to verify the main API endpoints, validation, and error handling.

---

## Future Improvements

If this project were extended further, possible improvements would include:

- Add an update (PUT/PATCH) endpoint
- Replace JSON storage with SQLite or PostgreSQL
- Add pagination and sorting for larger datasets
- Generate monthly spending summaries by category
- Add authentication so each user can manage their own expenses

---

## License

This project is licensed under the MIT License.