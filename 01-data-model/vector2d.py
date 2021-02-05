from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    # allows multiplication of 1 vector against a scaler value - v1 * 3
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    # allows multiplication of 2 vectors - v1*v2
    # def __mul__(self, v):
    #     return Vector(self.x * v.x, self.y * v.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
