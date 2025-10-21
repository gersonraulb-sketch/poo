class VehiculoBase:
    def encender(self): raise NotImplementedError


class Auto(VehiculoBase):
    def encender(self): return 'Auto encendido'


class Moto(VehiculoBase):
    def encender(self): return 'Moto encendida'
