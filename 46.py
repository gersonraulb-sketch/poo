class Profesor:
    def __init__(self, nombre): self.nombre = nombre


class EstudianteColegio:
    def __init__(self, nombre): self.nombre = nombre; self.notas = {}

    def agregar_nota(self, materia, nota): self.notas.setdefault(
        materia, []).append(nota)
