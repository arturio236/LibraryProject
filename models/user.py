from models.book import Book


class User:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books = []

    def to_dict(self) -> dict:
        """Converts a User instance into a dictionary."""
        return {"name": self.name, "borrowed_books": [book.to_dict() for book in self.borrowed_books]}

    @staticmethod
    def from_dict(source: dict):
        """Creates a User instance from a dictionary."""
        user = User(source["name"])
        user.borrowed_books = [Book.from_dict(book_dict) for book_dict in source["borrowed_books"]]
        return user
