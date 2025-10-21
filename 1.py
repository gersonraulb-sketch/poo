class Persona:
    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

    def presentarse(self):

        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

    def cumplir_años(self):

        self.edad += 1
