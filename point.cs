class Point:
    default_color = "green"  # like static

    def __init__(self, x, y):  # method should have at least one parameter self
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x}, {self.y})")

    @classmethod  # class level method
    def zero(cls):
        return cls(0, 0)


point = Point.zero()
point.draw()
point.z = 90

Point.default_color = "yellow"
print(point.default_color)
print(point.default_color)
