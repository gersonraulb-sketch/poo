class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, n):
        if 0 <= n <= 10:
            self.notas.append(n)

    def promedio(self):
        return sum(self.notas)/len(self.notas) if self.notas else 0
