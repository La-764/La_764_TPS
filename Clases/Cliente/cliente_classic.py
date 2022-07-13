from .cliente import Cuenta
from .cliente import Cliente

class ClienteClassic(Cliente):
    def __init__(self, monto, nombre, apellido, telefono, dni):
        super().__init__(monto, 10000, 150000, 1, 0, nombre, apellido, telefono, dni)