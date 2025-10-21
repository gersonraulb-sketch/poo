class MateriaSimple:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.registros = {}

    def inscribir(self, est): self.registros[est] = []
    def agregar_nota(self, est, nota): self.registros[est].append(nota)
