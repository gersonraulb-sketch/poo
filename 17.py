class SerVivo:
    def __init__(self, nombre): self.nombre = nombre


class Animal(SerVivo):
    def __init__(self, nombre, especie): super().__init__(
        nombre); self.especie = especie


class Mamifero(Animal):
    def __init__(self, nombre, especie, pelaje): super().__init__(
        nombre, especie); self.pelaje = pelaje
