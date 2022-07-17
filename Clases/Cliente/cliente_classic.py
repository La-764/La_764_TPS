from .cliente import Cliente
from .cuenta import CuentaDet

class ClienteClassic(Cliente):
    #def __init__(self, saldo, nombre, apellido, telefono, dni):
        #super().__init__(saldo, 10000, 150000, 1, 0, nombre, apellido, telefono, dni)
    
    def puede_comprar_dolar(self):
        return False
    def puede_tener_chequera(self):
        return False
    def puede_crear_tarjeta_credito(self):
        return False
    
    def cuenta_ahorro_pesos(self,monto):
        caja_ahorro_pesos = CuentaDet(10000,150000,monto,0.01*monto,0)
        return caja_ahorro_pesos
    