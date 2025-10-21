class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservas = []

    def esta_disponible(self, fi, ff):
        for (a, b, _) in self.reservas:
            if not (ff <= a or fi >= b):
                return False
        return True

    def reservar(self, fi, ff, huesped):
        if self.esta_disponible(fi, ff):
            self.reservas.append((fi, ff, huesped))
            return True
        return False
