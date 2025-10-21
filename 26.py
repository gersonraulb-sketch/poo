import math


class Calc:
    def potencia(self, b, e): return b**e

    def raiz(self, n):
        if n < 0:
            raise ValueError('negativo')
        return math.sqrt(n)

    def log(self, n, base=10): return math.log(n, base)
