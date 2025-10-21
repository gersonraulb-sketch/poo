class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.proyectos = []

    def agregar_empleado(self, e): self.empleados.append(e)
    def agregar_proyecto(self, p): self.proyectos.append(p)


if __name__ == '__main__':
    p = Persona('Ana', 25)
    print('1 -', p.presentarse())

    c = CuentaBancaria('Carlos', 100)
    c.depositar(50)
    c.retirar(30)
    print('2 - saldo', c.consultar_saldo())

    est = Estudiante('Luis')
    est.agregar_nota(8)
    est.agregar_nota(9)
    print('3 - promedio', est.promedio())

    carro = Carro('Toyota', 'Corolla', 4)
    carro.encender()
    print('4 -', carro.abrir_puertas())

    print('5 - perro', interactuar_con_animal(Perro()))
    print('6 - punto', Punto(1, 2) + Punto(3, 4))
    print('10 - factorial 5', Mat.factorial(5))
    print('44 - dados', Dados().lanzar(3))

    print('\nLista: archivo con 50 ejercicios creado en este archivo.')
