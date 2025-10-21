class Criatura:
    def __init__(self, nombre, tipo, vida=50):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida

    def recibir(self, dano): self.vida -= dano
