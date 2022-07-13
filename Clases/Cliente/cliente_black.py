from json.encoder import INFINITY
from .cliente import Cuenta
from .cliente import Cliente

class ClienteBlack(Cliente):
    def __init__(self, monto, nombre, apellido, telefono, dni):
        super().__init__(monto, 100000, INFINITY, 0, 10000, nombre, apellido, telefono, dni)
        #Cuidado con los ceros e infinitos que pueden dar problemas en las divisiones a futuro

    def puede_tener_chequera(self):
        return True

    def puede_crear_tarjeta_credito(self):
        return True

    def puede_comprar_dolar(self):
        return True