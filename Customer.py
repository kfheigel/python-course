class Customer:
    loyalty_levels = {"bronze", "gold", "platinum"}
    
    def __init__(self, loyalty, membership = 1):
        self.loyalty = loyalty
        self.membership = membership
        
    def get_membership(self):
        return self._membership
    
    def set_membership(self, value):
        if value <= 0 or value > 34:
            raise ValueError("Invalid membership years")    
        self._membership = value    
        
    def get_loyalty(self):
        return self._loyalty
    
    def set_loyalty(self, level):
        if level not in self.loyalty_levels:
            raise ValueError(f"Invalid loyalty {level} specified")
        self._loyalty = level
        
    loyalty = property(fget=get_loyalty, fset=set_loyalty)
    membership = property(fget=get_membership, fset=set_membership)

c1 = Customer("bronze")
c2 = Customer("gold", 30) 
c3 = Customer("platinum", 12)

def get_discount(customer):
    discounts = {
        "bronze": .1,
        "gold": .2,
        "platinum": .35
    }
    
    discount = discounts.get(customer.get_loyalty(), None)
    
    if not discount:
        raise ValueError("Could not determine the customer's discount")
    
    return discount

for customer in [c1, c2, c3]:
    print(f"Your discount is {get_discount(customer):.0%}")