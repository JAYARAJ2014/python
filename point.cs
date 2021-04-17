class Point:
    def __init__(self, x, y):  # method should have at least one parameter self
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x}, {self.y})")


point = Point(4, 5)
point.draw()
