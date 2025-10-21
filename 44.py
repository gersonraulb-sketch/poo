import random


class Dados:
    def lanzar(self, n=1): return [random.randint(1, 6) for _ in range(n)]
