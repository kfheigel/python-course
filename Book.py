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
        
    
b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)

print(repr(b))
eval(repr(b))
print(str(b))
print(b.__dict__)
