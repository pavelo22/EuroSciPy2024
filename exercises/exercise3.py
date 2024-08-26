class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __mul__(self, number):
        if isinstance(number, float | int):
            return Vector(self.x * number, self.y * number)
        else:
            return NotImplemented

    def __rmul__(self, number):
         return self.__mul__(number)        

    def __neg__(self):
        return ...  # <---- put your code here


v1 = Vector(10, 20)
v2 = Vector(50, 60)

v3 = v1 + v2

v4 = v3 * 3
assert str(v4) == str(Vector(180, 240))

v41 = 3 * v3
assert str(v41) == str(Vector(180, 240))

v5 = -v4
assert str(v5) == str(Vector(-180, -240))
