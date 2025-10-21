class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.vida = 100
        self.exp = 0

    def atacar(self, otro):
        dano = 10
        otro.vida -= dano
        self.exp += 5
        return dano

    def subir_nivel(self):
        if self.exp >= 100:
            self.nivel += 1
            self.exp = 0
            self.vida = 100
