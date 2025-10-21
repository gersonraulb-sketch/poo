class GestorArchivo:
    def __init__(self, nombre, modo='w'):
        self.nombre = nombre
        self.modo = modo

    def __enter__(self):
        self.f = open(self.nombre, self.modo)
        return self.f

    def __exit__(self, exc_type, exc, tb):
        self.f.close()
