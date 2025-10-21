class PacienteMed:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.citas = []


class DoctorMed:
    def __init__(self, nombre): self.nombre = nombre; self.citas = []


class Cita:
    def __init__(self, paciente, doctor, fecha):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.estado = 'Programada'
