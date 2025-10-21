class EmpleadoBase:
    def __init__(
            self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_salario(self): return self.salario


class EmpleadoPorHoras(EmpleadoBase):
    def __init__(self, nombre, tarifa, horas): super().__init__(
        nombre, 0); self.tarifa = tarifa; self.horas = horas

    def calcular_salario(self): return self.tarifa*self.horas
