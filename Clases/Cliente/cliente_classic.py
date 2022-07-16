from .cliente import Cliente

class ClienteClassic(Cliente):
    def __init__(self, saldo, nombre, apellido, telefono, dni, transacciones=[]):
        super().__init__(saldo, 10000, 150000, 1, 0, nombre, apellido, telefono, dni, transacciones)
    
    def puede_comprar_dolar(self):
        return False
    def puede_tener_chequera(self):
        return False
    def puede_crear_tarjeta_credito(self):
        return False