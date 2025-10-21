import json


class GestorDatos:
    def __init__(self, nombre): self.nombre = nombre; self.datos = []
    def agregar(self, **k): self.datos.append(k)

    def guardar(self):
        with open(self.nombre+'.json', 'w', encoding='utf-8') as f:
            json.dump(self.datos, f, ensure_ascii=False)

    def cargar(self):
        with open(self.nombre+'.json', 'r', encoding='utf-8') as f:
            self.datos = json.load(f)
