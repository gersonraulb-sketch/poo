from datetime import datetime


class ProductoInv:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = 0
        self.hist = []

    def agregar_stock(self, cantidad):
        self.stock += cantidad
        self.hist.append((datetime.now(), 'ENTRADA', cantidad))

    def reducir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            self.hist.append((datetime.now(), 'SALIDA', cantidad))
            return True
        return False
