from multiprocessing.sharedctypes import Value
from .cliente import Cuenta


class Cliente(Cuenta):
    def __init__(self, monto, limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible, nombre, apellido, telefono, dni):
        super().__init__(monto, limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible)
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        try:
            strNombre = str(nombre)
            self.__nombre = strNombre
        except ValueError as err:
            raise ValueError("El nombre debe ser texto o debe poder ser convertido a texto")
        except TypeError:
            raise TypeError("El nombre debe ser texto o debe poder ser convertido a texto")
        except:
            raise
        finally:
            return "Nombre: " + str(self.__nombre)

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        try:
            strApellido = str(apellido)
            self.__apellido = strApellido
        except ValueError:
            raise ValueError("El apellido debe ser texto o debe poder ser convertido a texto")
        except TypeError:
            raise TypeError("El apellido debe ser texto o debe poder ser convertido a texto")
        except:
            raise
        finally:
            return "Apellido: " + str(self.__apellido)

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        try:
            intTelefono = int(telefono)
            self.__telefono = intTelefono
        except ValueError:
            raise ValueError("El telefono debe ser un numero o poder ser convertido en un numero")
        except TypeError:
            raise TypeError("El telefono debe ser un numero o poder ser convertido en un numero")
        except:
            raise
        finally:
            return "Telefono: " + str(self.__telefono)

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        try:
            intDni = int(dni)
            self.__dni = intDni
        except ValueError:
            raise ValueError("El dni debe ser un numero o poder ser convertido en un numero")
        except TypeError:
            raise TypeError("El dni debe ser un numero o poder ser convertido en un numero")
        except:
            raise
        finally:
            return "DNI: " + str(self.__dni)
    
    def puede_tener_chequera(self):
        return False
    
    def max_chequera(self):
        return 0

    def puede_crear_tarjeta_credito(self):
        return False

    def max_tarjeta_credito(self):
        return 0

    def puede_comprar_dolar(self):
        return False