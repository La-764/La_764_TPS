class Cliente:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def puede_tener_chequera(self):
        return False

    @property
    def nombre(self):
        return str(self.__class__) + ": " + str(self.__nombre)

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre