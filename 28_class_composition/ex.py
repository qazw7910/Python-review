class BookSelf:

    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'BookSelf with {self.quantity} books.'


# self = BookSelf(300)
# print(self)

class Book(BookSelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name


# This makes no sense, because now you need to pass `quantity` to a single book:
# book = Book("Harry Potter", 120)
# print(book)

# -- Composition over inheritance here --

# Inheritance: "A Book is a BookShelf"
# Composition: "A BookShelf has many Books"


class BookShelf:

    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f'BookShelf with {len(self.books)} books'


class Book:

    def __init__(self, name):
        self.name = name

book = Book('Harry Potter')
book2 = Book('python 101')
shef = BookShelf(book,book2)
print(shef)