from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

books = [
    {
        "id": 1,
        "title": "Atomic Habits",
        "author": "James Clear",
        "publish_date": "2018-10-16",
        "copies_sold": "1M"
    
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "publish_date": "1949-06-08",
        "copies_sold": "5.5lakh"
    },
    {
        "id": 3,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publish_date": "1960-07-11",
        "copies_sold": "8lakh"
    },
    {
        "id": 4,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "publish_date": "1937-09-21",
        "copies_sold": "4.1lakh"
    },
        {
        "id": 5,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publish_date": "1813-01-28"
    },
]

app = FastAPI()

@app.get('/book')
def get_book():
    return books

@app.get('/book/{book_id}')
def get_bookby_id(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book not found")

class Book(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str

@app.post('/book')
def add_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book

class BookUpdate(BaseModel):
    title: str
    author: str
    publish_date: str

@app.put('/book/{book_id}')
def book_update(book_id: int, book_update: BookUpdate):
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update.title
            book["author"] = book_update.author
            book["publish_date"] = book_update.publish_date
            return book

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book not Found")
     
@app.delete('/book/{book_id}')
def book_delete(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return book
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book not Found")