class ItemCarrito:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self): return self.producto.precio*self.cantidad


class Carrito:
    def __init__(self): self.items = []
    def agregar(self, item): self.items.append(item)
    def total(self): return sum(i.subtotal() for i in self.items)
