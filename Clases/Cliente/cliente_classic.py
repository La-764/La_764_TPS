from .cliente import Cuenta
from .cliente import Cliente

class ClienteClassic(Cliente):
    def __init__(self, saldo, nombre, apellido, telefono, dni):
        super().__init__(saldo, 10000, 150000, 1, 0, nombre, apellido, telefono, dni)