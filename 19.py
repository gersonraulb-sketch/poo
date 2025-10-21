class Vector:
    def __init__(self, x, y): self.x = x; self.y = y
    def __str__(self): return f"Vector({self.x},{self.y})"
    def __eq__(self, otro): return (self.x, self.y) == (otro.x, otro.y)
