class Contact():
    def __init__(self, name, last_name, phone=None, email=None, display_mode = "masked") -> None:
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.display_mode = display_mode
    
    def __repr__(self) -> str:
        if self.display_mode == 'masked':
            return f"Contact(name='{self._obfuscate(self.name)}', last_name='{self._obfuscate(self.last_name)}')"
        return f"Contact(name='{self.name}', last_name='{self.last_name}', phone='{self.phone}', email='{self.email}')"
    
    def __str__(self) -> str:
        return f"{self.last_name[0]}{self.name[0]}"
        
    def __format__(self, __format_spec: str) -> str:
        if __format_spec != 'masked':
            return f"Contact(name={self.name}, last_name={self.last_name}, phone={self.phone}, email={self.email})"
        
        return repr(self)
    
    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False
        if (self.phone is not None and self.phone == other.phone) or \
            (self.email is not None and self.email == other.email):
            return True
        if self.name == other.name and self.last_name == other.last_name:
            return True
        return False
    
    def __hash__(self) -> int:
        return hash((self.name, self.last_name, self.phone, self.email))
    
    @staticmethod
    def _obfuscate(text):
        half_length = len(text) // 2
        return text[:half_length] + '*' * (half_length + 1)
    
c1 = Contact("Andy", "Bek")
c2 = Contact("Andy", "Bek", "666555666")
c3 = Contact("Andy", "Bek", "666555666", 'hey@andybek.com')
c4 = Contact("Andy", "Bek", "666555666", 'hey@andybek.com', display_mode="show")

print(c1 == c2)
print(repr(c1))
print(str(c1))
print(f"{c1:unmasked}")
print("{c:unmasked}".format(c=c2))
print(format(c3, "unmasked"))
    