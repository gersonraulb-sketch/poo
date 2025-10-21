class Libro:
    def __init__(self, isbn, titulo): self.isbn = isbn
    self.titulo = titulo
    self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self): self.disponible = True


class Biblioteca:
    def __init__(self): self.libros = {}
    def agregar(self, l): self.libros[l.isbn] = l

    def buscar(self, t): return [
        l for l in self.libros.values() if t.lower() in l.titulo.lower()]


y
