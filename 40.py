class Parada:
    def __init__(self, nombre): self.nombre = nombre; self.pasajeros = []


class BusSimple:
    def __init__(self, numero): self.numero = numero; self.pasajeros = []
    def subir(self, p): self.pasajeros.append(p)
    def bajar(self, p): self.pasajeros.remove(p)
