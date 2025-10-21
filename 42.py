class Mensaje:
    def __init__(self, emisor, texto): self.emisor = emisor; self.texto = texto


class Chat:
    def __init__(self): self.mensajes = []
    def enviar(self, m): self.mensajes.append(m)
