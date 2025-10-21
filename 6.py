class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Punto(self.x+otro.x, self.y+otro.y)

    def __str__(self):
        return f"Punto({self.x}, {self.y})"
