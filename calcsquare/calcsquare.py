import math


def calculate(radius, x, y, z):
    """
    Print an area of a figure.
    Args:
        radius (int): radius of a circle
        x (int) : 1st side of a triangle
        y (int) : 2nd side of a triangle
        z (int) : 3rd side of a triangle
    Returns:
        circle_square (float): area of a circle
        triangle_square (float): area of a triangle
    """

    circle_square = math.pi * radius**2
    halfperimeter = (x + y + z) / 2
    triangle_square = math.sqrt(halfperimeter * (halfperimeter - x) * (halfperimeter - y) * (halfperimeter - z))
    return circle_square, triangle_square
