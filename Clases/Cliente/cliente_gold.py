from re import sub
from .cliente import Cliente
from .cuenta import CuentaDet

class ClienteGold(Cliente):
    #def __init__(self, saldo, nombre, apellido, telefono, dni):
        #super().__init__(saldo, 20000, 500000, 0.5, 10000, nombre, apellido, telefono, dni)

    def tiene_cuenta_dolares(self):
        return True

    def puede_comprar_dolar(self):
        return True

    def tiene_cuenta_corriente(self):
        return True
    
    def puede_tener_chequera(self):
        return True

    def max_chequera(self):
        return 1

    def puede_crear_tarjeta_credito(self):
        return True

    def max_tarjeta_credito(self):
        return 1

    def cuenta_ahorro_pesos(self,monto):
        caja_ahorro_pesos = CuentaDet(20000,500000,monto,0.005*monto,0)
        return caja_ahorro_pesos
    
    def cuenta_corriente(self,monto):
        cuenta_corriente = CuentaDet(20000,500000,monto,0.005*monto,10000)
        return cuenta_corriente

    def cuenta_ahorro_dolares(self,monto):
        caja_ahorro_dolar = CuentaDet(2000,500000,monto,monto*0.005,0) 
        return caja_ahorro_dolar

    
