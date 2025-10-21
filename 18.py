class Volador:
    pass


class Nadador:
    pass


class Pato(Animal, Volador, Nadador):
    def __init__(self, nombre): Animal.__init__(self, nombre, 'Pato')
