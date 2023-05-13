class Book:
    def __init__(self, title: str, author: str, available: bool = True):
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self) -> dict:
        """Converts a Book instance into a dictionary."""
        return {"title": self.title, "author": self.author, "available": self.available}

    @staticmethod
    def from_dict(source: dict):
        """Creates a Book instance from a dictionary."""
        return Book(source["title"], source["author"], source["available"])
