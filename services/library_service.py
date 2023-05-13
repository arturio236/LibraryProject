import json
from typing import List
from models.book import Book
from models.user import User

class LibraryService:
    def __init__(self, db_file: str):
        self.db_file = db_file
        self.books = []
        self.users = []

    def load_data(self):
        """Loads data from the JSON file into memory."""
        try:
            with open(self.db_file, "r") as file:
                data = json.load(file)
                self.books = [Book.from_dict(book_dict) for book_dict in data.get("books", [])]
                self.users = [User.from_dict(user_dict) for user_dict in data.get("users", [])]
        except FileNotFoundError:
            self.books = []
            self.users = []

    def save_data(self):
        """Saves data from memory into the JSON file."""
        with open(self.db_file, "w") as file:
            data = {
                "books": [book.to_dict() for book in self.books],
                "users": [user.to_dict() for user in self.users],
            }
            json.dump(data, file)

    def add_book(self, title: str, author: str):
        """Adds a new book to the library."""
        self.books.append(Book(title, author))
        self.save_data()

    def remove_book(self, title: str):
        """Removes a book from the library."""
        self.books = [book for book in self.books if book.title != title]
        self.save_data()

    def borrow_book(self, user_name: str, book_title: str):
        """A user borrows a book from the library."""
        user = next((user for user in self.users if user.name == user_name), None)
        if not user:
            user = User(user_name)
            self.users.append(user)

        book = next((book for book in self.books if book.title == book_title and book.available), None)
        if book:
            book.available = False
            user.borrowed_books.append(book)
            self.save_data()

    def return_book(self, user_name: str, book_title: str):
        """A user returns a book to the library."""
        user = next((user for user in self.users if user.name == user_name), None)
        if not user:
            return

        book = next((book for book in user.borrowed_books if book.title == book_title), None)
        if book:
            book.available = True
            user.borrowed_books.remove(book)
            self.save_data()
