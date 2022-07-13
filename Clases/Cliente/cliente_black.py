from .cliente import Cliente

class ClienteBlack(Cliente):
    def __init__(self, nombre):
        super().__init__(nombre)

    def puede_tener_chequera(self):
        return True