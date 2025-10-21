class Contador:
    def __init__(self, inicio, fin, paso=1):
        self.inicio = inicio
        self.fin = fin
        self.paso = paso

    def __iter__(self):
        self.actual = self.inicio
        return self

    def __next__(self):
        if self.actual < self.fin:
            v = self.actual
            self.actual += self.paso
            return v
        raise StopIteration
