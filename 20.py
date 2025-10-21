class Empleado:
    def __init__(self, nombre): self.nombre = nombre; self.departamento = None


class Departamento:
    def __init__(self, nombre): self.nombre = nombre; self.empleados = []

    def agregar(self, e): self.empleados.append(
        e); e.departamento = self.nombre
