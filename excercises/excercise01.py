class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __mul__(self, number):
        return ...  # <---- put your answer here
        
v1 = Vector(10, 20)
v2 = Vector(50, 60)

v3 = v1 + v2
v4 = v3 * 3
assert str(v4) == str(Vector(180, 240))
