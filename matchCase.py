class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        # the “variable name” _ acts as a wildcard and never fails to match. If no case matches, none of the branches is executed.
        case _:
            print("Not a point")


where(Point(1, 2))
where(Point(0, 5))
where(Point(0, 0))
where(Point)
