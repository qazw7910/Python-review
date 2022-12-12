def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)


# -- Type hinting classes --

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count


# -- Lists and collections --

from typing import List


class BookShelf:

    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f'BookShelf with {len(self.books)} books.'


# Key benefit is now you'll get told if you pass in the wrong thing...
book = Book("Harry Potter", "352")

shelf = BookShelf(book)  # Suggests this is incorrect too


# Type hinting is that: hints. It doesn't stop your code from working... although it can save you at times!

# -- Hinting the current object --

class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f'<Book {self.name}, {self.book_type}, weght {self.weight}g>'

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> 'Book':
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def papercover(cls, name: str, page_weight: int) -> 'Book':
        return cls(name, cls.TYPES[1], page_weight)
