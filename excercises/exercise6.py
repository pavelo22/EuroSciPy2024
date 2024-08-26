class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __dir__(self):
        return dir(self)

v1 = Vector(1, 2)
print(dir(v1))
