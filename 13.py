class SaldoInsuficiente(Exception):
    pass


class CuentaSegura(CuentaBancaria):
    def retirar_seguro(self, cantidad):

        if cantidad > self.consultar_saldo():
            raise SaldoInsuficiente('Saldo insuficiente')
        return self.retirar(cantidad)
