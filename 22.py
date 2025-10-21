class Observable:
    def __init__(self): self.obs = []
    def suscribir(self, o): self.obs.append(o)

    def notificar(self, d):
        for o in self.obs:
            o.actualizar(d)


class Observador:
    def actualizar(self, d): print('recibido', d)
