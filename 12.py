class GestorProductos:
    def __init__(self): self.productos = []
    def agregar(self, p): self.productos.append(p)

    def filtrar(self, categoria): return [
        p for p in self.productos if p.categoria == categoria]
