from collections import namedtuple
from functools import total_ordering

@total_ordering
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
    
    def __hash__(self) -> int:
        return hash(tuple((self.title, self.author)))
    
    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages > other.pages

    def __len__(self):
        return self.pages if self.pages > 0 else 0
    
    # def __bool__(self):
    #     return bool(self.pages) and not (self.pages<1)
    
    # def __lt__(self, other):
    #     return NotImplemented
    
    # def __le__(self, other):
    #     if not isinstance(other, Book):
    #         return NotImplemented
    #     return self.pages <= other.pages
    
    # def __ge__(self, other):
    #     return NotImplemented

    # def __ne__(self, other):
    #     print("comparing non-equality")

essay = namedtuple("essay", ["title", "author"])

e = essay("Antifragile", "Nassim Taleb")

b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
b2 = Book("Antifragile", "Nassim Taleb", "Hardcover", 472)

# print(bool(b))
# print(b == b2)
# print(b != b2)
# print(b > b2)
# print(b < b2)
# print(b >= b2)
# print(b <= b2)
# print(b == e)
# print(b != e)
# print(repr(b))
# eval(repr(b))
# print(str(b))
# print(b.__dict__)

# print(f"{b:stealth}")
# print("{:short}".format(b))
# print(format(b, "stealth"))
