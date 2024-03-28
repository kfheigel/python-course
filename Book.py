from collections import namedtuple


class Book:
    def __init__(self, title, author, book_type, pages) -> None:
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages

    def __repr__(self) -> str:
        return f"Book('{self.author}', '{self.title}', '{self.book_type}', {self.pages})"

    def __str__(self) -> str:
        return f"{self.title} by {self.author} in {self.book_type}"

    def __format__(self, format_spec):
        if format_spec == "short":
            return f"{self.title} - {self.author}"
        elif format_spec == "stealth":
            return f"A book contain {self.pages}. Guess?"

        return repr(self)

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author


essay = namedtuple("essay", ["title", "author"])

e = essay("Antifragile", "Nassim Taleb")

b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
b2 = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)

print(b == e)
# print(repr(b))
# eval(repr(b))
# print(str(b))
# print(b.__dict__)

# print(f"{b:stealth}")
# print("{:short}".format(b))
# print(format(b, "stealth"))
