import math


class Calculator:
    def __init__(self):
        pass

    # circle method - given radius, return the circle square
    def circle(self, radius):
        return math.pi * radius**2

    # triangle method - given 3 sides, return the triangle square
    def triangle(self, x, y, z):
        if (math.sqrt(x ** 2) == math.sqrt(y ** 2 + z ** 2) or
            math.sqrt(y ** 2) == math.sqrt(x ** 2 + z ** 2) or
            math.sqrt(z ** 2) == math.sqrt(x ** 2 + y ** 2)):
            print("Right triangle")

        halfperimeter = (x + y + z) / 2
        triangle_square = math.sqrt(halfperimeter * (halfperimeter - x) * (halfperimeter - y) * (halfperimeter - z))
        return triangle_square

    def new_figure(self, a, b):
        return a * b
