# AI Usage Notes

## How I Used AI

I used AI as a learning and debugging tool while building this project.

Rather than generating the entire project at once, I built it feature by feature. AI helped me understand FastAPI concepts, discuss different implementation approaches, and troubleshoot issues that came up during development.

---

## Where AI Helped

AI was mainly used for:

- Understanding how to organize a FastAPI project into separate modules.
- Clarifying FastAPI and Pydantic concepts.
- Discussing REST API design and endpoint structure.
- Debugging errors encountered during development.
- Reviewing the project after the core functionality was complete.
- Improving the README and project documentation.

---

## What I Verified Myself

I verified every feature before moving on to the next one.

This included:

- Testing each endpoint using the FastAPI Swagger UI.
- Running automated tests with pytest.
- Checking request validation using both valid and invalid inputs.
- Fixing issues discovered during testing instead of assuming suggested code was correct.

Several parts of the implementation changed during development as I tested and refined the project.

---

## Decisions I Made

Although AI suggested different approaches, I made the final implementation decisions based on the assignment requirements.

For example:

- I chose JSON file storage because it matched the project requirements and kept the implementation simple.
- I organized the project into routes, services, storage, and schemas to keep responsibilities separated.
- I intentionally kept the implementation focused on the required API functionality instead of adding features such as authentication or a database that were outside the scope of the assignment.

## What I Learned

Building this project helped me become more comfortable with:

- Designing REST APIs using FastAPI.
- Request validation with Pydantic.
- Organizing backend code into separate layers.
- Writing automated API tests using pytest.
- Debugging and testing backend applications.