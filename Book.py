class Book:
    def __init__(self, title, author, book_type, pages) -> None:
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
        
    def __repr__(self) -> str:
        return f"The Title is {self.title}"
        
    
b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
print(b)
