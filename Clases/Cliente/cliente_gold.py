from re import sub
from .cliente import Cliente

class ClienteGold(Cliente):
    def __init__(nombre, apellido, telefono, dni):
        super().__init__(nombre, apellido, telefono, dni)

    def puede_tener_chequera(self):
        return True

    def puede_crear_tarjeta_credito(self):
        return True

    def puede_comprar_dolar(self):
        return True