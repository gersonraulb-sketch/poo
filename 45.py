class Pedido:
    def __init__(self, cliente, items):
        self.cliente = cliente
        self.items = items

    def total(self): return sum(i.subtotal() for i in self.items)
