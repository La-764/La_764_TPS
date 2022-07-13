from re import sub
from .cliente import Cliente

class ClienteGold(Cliente):
    def __init__(nombre, apellido, telefono, dni):
        super().__init__(nombre, apellido, telefono, dni)

    def puede_tener_chequera(self):
        return True