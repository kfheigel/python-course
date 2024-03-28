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
        
    
b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)

# print(repr(b))
# eval(repr(b))
# print(str(b))
# print(b.__dict__)

print(f"{b:stealth}")
print("{:short}".format(b))
print(format(b, "stealth"))
