class ArchivoVirtual:
    def __init__(self, nombre, contenido=''):
        self.nombre = nombre
        self.contenido = contenido

    def tam(self): return len(self.contenido)


class CarpetaVirtual:
    def __init__(self, nombre): self.nombre = nombre; self.elementos = {}
    def agregar(self, e): self.elementos[e.nombre] = e
    def listar(self): return list(self.elementos.keys())
