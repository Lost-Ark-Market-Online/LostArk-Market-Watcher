class Rect():
    x1: int
    y1: int
    x2: int
    y2: int

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def add(self, x1, y1, x2, y2):
        return Rect(self.x1+x1, self.y1+y1, self.x2+x2, self.y2+y2)
