class MetodoPagoBase:
    def procesar(self, monto): raise NotImplementedError


class Tarjeta(MetodoPagoBase):
    def __init__(self, limite): self.limite = limite; self.usado = 0

    def procesar(self, monto):
        if monto <= self.limite-self.usado:
            self.usado += monto
            return True
        return False


class CuentaPago(MetodoPagoBase):
    def __init__(self, saldo): self.saldo = saldo

    def procesar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        return False
