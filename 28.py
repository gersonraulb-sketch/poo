import random


class Carta:
    def __init__(self, palo, valor): self.palo = palo; self.valor = valor
    def __str__(self): return f"{self.valor} de {self.palo}"


class Baraja:
    def __init__(self):
        palos = ['C', 'D', 'T', 'E']
        vals = [str(i) for i in range(1, 11)]+['J', 'Q', 'K']
        self.cartas = [Carta(p, v) for p in palos for v in vals]

    def mezclar(self): random.shuffle(self.cartas)
    def repartir(self): return self.cartas.pop() if self.cartas else None
