# FastAPI CRUD Application

A simple CRUD (Create, Read, Update, Delete) REST API built using FastAPI and Python.

## Features

- Get all books
- Get a book by ID
- Add a new book
- Update existing book details
- Delete a book
- Exception handling using HTTPException
- Data validation using Pydantic

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /book | Get all books |
| GET | /book/{book_id} | Get book by ID |
| POST | /book | Add new book |
| PUT | /book/{book_id} | Update book |
| DELETE | /book/{book_id} | Delete book |

## Installation

### Clone Repository

```bash
git clone https://github.com/sindhurametla/fastapicrud.git
cd fastapicrud
