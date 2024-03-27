class MercedesBenz:
    doors = 4
    model = 'G'
    wheels = 4
    
    def __init__(self, color="black"):
        self.color = color
    
    def drive(self):
        return f"A Mercedes is driving. It is {self}\n"
    
    @staticmethod
    def auto_drive():
        return "Auto-driving for now..."
    
    @classmethod
    def create_lease(cls):
        print(f"A lease for {cls} will be created")