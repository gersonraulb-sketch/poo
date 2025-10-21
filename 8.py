class Inventario:
    def __init__(self):
        self.productos = {}  # nombre: cantidad

    def agregar(self, nombre, cantidad):
        self.productos[nombre] = self.productos.get(nombre, 0)+cantidad

    def bajo_stock(self, minimo=5):
        return [n for n, c in self.productos.items() if c < minimo]
