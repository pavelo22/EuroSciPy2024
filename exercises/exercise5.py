class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
        

v1 = Vector(1, 2)
print(...) # <---- put your code here
print(...) # <---- put your code here