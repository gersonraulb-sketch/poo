class Perro:
    def hacer_sonido(self):
        return "Guau"


class Gato:
    def hacer_sonido(self):
        return "Miau"


def interactuar_con_animal(a):
    return a.hacer_sonido()
