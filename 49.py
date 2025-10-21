class Vuelo:
    def __init__(self, codigo, origen, destino):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.asientos = []

    def reservar(self, asiento, usuario):
        if asiento in self.asientos:
            return False
        self.asientos.append(asiento)
        return True
