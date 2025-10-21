class Tarea:
    def __init__(self, nombre, fecha_limite, prioridad='Media'):
        self.nombre = nombre
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.completada = False

    def completar(self): self.completada = True
