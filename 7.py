class Calificador:
    def __init__(self):
        self.notas = []

    def agregar(self, n):
        if 0 <= n <= 100:
            self.notas.append(n)

    def letra(self):
        prom = sum(self.notas)/len(self.notas) if self.notas else 0
        if prom >= 90:
            return 'A'
        if prom >= 80:
            return 'B'
        if prom >= 70:
            return 'C'
        if prom >= 60:
            return 'D'
        return 'F'
