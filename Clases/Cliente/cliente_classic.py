from .cliente import Cliente

class ClienteClassic(Cliente):
    def __init__(self, nombre, apellido, telefono, dni):
        super().__init__(nombre, apellido, telefono, dni)