class Ser:
    def __init__(self, n): self.nombre = n; self.energia = 100
    def esta_vivo(self): return self.energia > 0


class Planta(Ser):
    def fotosintesis(self): self.energia += 10


class AnimalE(Ser):
    def comer(self, otro):
        if isinstance(otro, Planta):
            self.energia += 20
            return True
        return False
