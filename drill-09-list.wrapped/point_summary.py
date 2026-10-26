""" Implement point_summary(point). The point argument is a tuple containing x and y. Return a dictionary with keys named x, y, and manhattan. The manhattan value is the absolute value of x plus the absolute value of y."""
def point_summary(point):
    x, y = point

    manhattan = abs(x) + abs(y)

    return {
        "x": x,
        "y": y,
        "manhattan": manhattan
    }

print(point_summary((-3, 4)))
# {'x': -3, 'y': 4, 'manhattan': 7}

print(point_summary((2, 5)))
# {'x': 2, 'y': 5, 'manhattan': 7}

print(point_summary((0, 0)))
# {'x': 0, 'y': 0, 'manhattan': 0}

print(point_summary((-2, -6)))
# {'x': -2, 'y': -6, 'manhattan': 8}