from json.encoder import INFINITY
from .cliente import Cliente
from .cuenta import CuentaDet

class ClienteBlack(Cliente):
    #def __init__(self, saldo, nombre, apellido, telefono, dni):
        #super().__init__(saldo, 100000, INFINITY, 0, 10000, nombre, apellido, telefono, dni)
        #Cuidado con los ceros e infinitos que pueden dar problemas en las divisiones a futuro

    def tiene_cuenta_dolares(self):
        return True

    def puede_comprar_dolar(self):
        return True
        
    def tiene_cuenta_corriente(self):
        return True
    
    def puede_tener_chequera(self):
        return True

    def max_chequera(self):
        return 2

    def puede_crear_tarjeta_credito(self):
        return True

    def max_tarjeta_credito(self):
        return 5
    
    def cuenta_ahorro_pesos(self,monto):
        caja_ahorro_pesos = CuentaDet(100000,None,500000,monto,0,0)
        return caja_ahorro_pesos
    
    def cuenta_corriente(self,monto):
        cuenta_corriente = CuentaDet(100000,None,monto,0,10000)
        return cuenta_corriente

    