class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False


class Carro(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def abrir_puertas(self):
        return f"Abriendo {self.puertas} puertas"
