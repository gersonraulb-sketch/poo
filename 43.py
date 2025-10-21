class Cliente:
    def __init__(self, nombre): self.nombre = nombre; self.cuentas = []


class CuentaSimple:
    def __init__(self, balance=0): self.balance = balance

    def transferir(self, otra, monto):
        if monto <= self.balance:
            self.balance -= monto
            otra.balance += monto
            return True
        return False
