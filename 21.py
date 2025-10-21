class Circulo:
    pass


class Rectangulo:
    pass


class Fabrica:
    @staticmethod
    def crear(tipo, *a):
        if tipo == 'circulo':
            return Circulo()
        if tipo == 'rectangulo':
            return Rectangulo()
        raise ValueError('Tipo')
