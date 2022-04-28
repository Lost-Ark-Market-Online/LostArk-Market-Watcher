class Point():
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        return Point(self.x+x, self.y+y)
