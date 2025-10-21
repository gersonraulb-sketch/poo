class SistemaAcceso:
    def __init__(self):
        self.usuarios = {'admin': '123'}
        self.intentos = {}

    def login(self, user, passw):
        if self.intentos.get(user, 0) >= 3:
            return False
        if self.usuarios.get(user) == passw:
            self.intentos[user] = 0
            return True
        self.intentos[user] = self.intentos.get(user, 0)+1
        return False
