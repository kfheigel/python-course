from functools import total_ordering
import math

@total_ordering
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y       
        self.z = z

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z}))"
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Operation only supported between instances of vector")
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
        if not type(other) == int and not type(other) == float:
            raise TypeError("Operation only supported for a numeric scalar")
        return Vector(self.x * other, self.y * other, self.z * other)
    
    def __rmul__(self, other):
        return self * other
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Vector):
            return False
    
        return self.x == __value.x and self.y == __value.y and self.z == __value.z
    
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))
    
    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y**2 + self.z**2)
        # return math.hypot(self.x, self.y, self.z)
    
    def __le__(self, __value: object) -> bool:
        if not isinstance(__value, Vector):
            return TypeError("Must be a vector")
    
        return abs(self) < abs(__value)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __getitem__(self, item):
        if type(item) == str and item.lower() in ['x', 'y', 'z']:
            return eval(f"self.{item.lower()}")
        else:
            return NotImplemented
        
v1 = Vector(1,2,3)
v2 = Vector(2,3,6)
v3 = Vector(0,0,0)

print(bool(v1))
print(bool(v3))
print(v1+v2)
print(v2*2)
print(v1<v2)
print(v1<=v2)
print(v1>v2)
print(v1['X'])
print(v1['pandas'])

