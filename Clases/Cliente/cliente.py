from multiprocessing.sharedctypes import Value
from direccion import DireccionDesc
from transacciones import TransaccionesDet

class Cliente:
    def __init__(self, saldo, limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible, nombre, apellido, telefono, dni, transacciones) -> None:
       
        self.__saldo = saldo
        self.__limite_extraccion_diario = limite_extraccion_diario
        self.__limite_transferencia_recibida = limite_transferencia_recibida
        self.__costo_transferencias = costo_transferencias
        self.__saldo_descubierto_disponible = saldo_descubierto_disponible
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__dni = dni
        self.__transacciones = TransaccionesDet()
        self.__direccion = DireccionDesc()

        self.__tarjeta_credito = 0

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
    @property
    def transacciones(self):
        return self.__transacciones

    def get_saldo(self):
        return self.__monto

    def set_saldo(self, saldo):
        try:
            floatSaldo = float(saldo)
            self.__saldo = floatSaldo
        except ValueError:
            raise ValueError("El saldo debe ser un numero o poder ser convertido en un numero")
        except TypeError:
            raise TypeError("El saldo debe ser un numero o poder ser convertido en un numero")
        except:
            raise
        finally:
            return "Saldo: " + str(self.__saldo)

    def get_limite_extraccion_diario(self):
        return self.__limite_extraccion_diario

    def set_limite_extraccion_diario(self, limite_extraccion_diario):
        try:
            floatLimiteExtraccionDiario = float(limite_extraccion_diario)
            self.__monto = floatLimiteExtraccionDiario
        except ValueError:
            raise ValueError("El límite de extracción diario debe ser un numero o poder ser convertido en un numero")
        except TypeError:
            raise TypeError("El límite de extracción diario debe ser un numero o poder ser convertido en un numero")
        except:
            raise
        finally:
            return "Limite de extracción diario: " + str(self.__limite_extraccion_diario)

    def get_limite_transferencia_recibida(self):
        return self.__limite_transferencia_recibida

    def set_limite_transferencia_recibida(self, limite_transferencia_recibida):
        try:
            floatLimiteTransferenciaRecibida = float(limite_transferencia_recibida)
            self.__limite_transferencia_recibida = floatLimiteTransferenciaRecibida
        except ValueError:
            raise ValueError("El límite de transferencia recibida debe ser un numero o poder ser convertido en un numero")
        except TypeError:
            raise TypeError("El límite de transferencia recibida debe ser un numero o poder ser convertido en un numero")
        except:
            raise
        finally:
            return "Limite transferencia recibida: " + str(self.__limite_transferencia_recibida)

    def get_costo_transferencias(self):
        return self.__costo_transferencias

    def set_costo_transferencias(self, costo_transferencias):
        try:
            floatCostoTransferencias = float(costo_transferencias)
            self.__costo_transferencias = floatCostoTransferencias
        except ValueError:
            raise ValueError("El costo de transferencias debe ser un numero o poder ser convertido en un numero")
        except TypeError:
            raise TypeError("El costo de transferencias debe ser un numero o poder ser convertido en un numero")
        except:
            raise
        finally:
            return "Costo de transferencias: " + str(self.__costo_transferencias)

    def get_saldo_descubierto_disponible(self):
        return self.__saldo_descubierto_disponible

    def set_saldo_descubierto_disponible(self, saldo_descubierto_disponible):
        try:
            floatSaldoDescubiertoDisponible = float(saldo_descubierto_disponible)
            self.__saldo_descubierto_disponible = floatSaldoDescubiertoDisponible
        except ValueError:
            raise ValueError("El saldo descubierto disponible debe ser un numero o poder ser convertido en un numero")
        except TypeError:
            raise TypeError("El saldo descubierto disponible debe ser un numero o poder ser convertido en un numero")
        except:
            raise
        finally:
            return "Saldo descubierto disponible: " + str(self.__saldo_descubierto_disponible)

    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def set_direccion(self, direccion):
        self.__direccion = direccion
    
    def tiene_cuenta_pesos(self):
        return True

    def tiene_cuenta_dolares(self):
        return False

    def puede_comprar_dolar(self):
        pass

    def tiene_cuenta_corriente(self):
        return False

    def puede_tener_chequera(self):
        return False
    
    def max_chequera(self):
        return 0

    def puede_crear_tarjeta_credito(self):
        return False

    def max_tarjeta_credito(self):
        return 0

    def puede_retirar_x_monto(self, retiro):
        return retiro <= self.__limite_extraccion_diario and retiro <= (self.__saldo + self.__saldo_descubierto_disponible)

    def puede_crear_credito(self):
        return self.__tarjeta_credito <= self.max_tarjeta_credito
'''
RETIRO_EFECTIVO_CAJERO_AUTOMATICO: Tener presente que si tiene
cuenta corriente puede figurar el valor de saldo en cuenta como negativo
hasta el importe del cupo establecido
  ALTA_TARJETA_CREDITO: Se solicito una nueva tarjeta de crédito
  ALTA_CHEQUERA: Se solicito una nueva chequera
  COMPRAR_DOLAR: Se solicito realizar la transacción para comprar
dólares, pero solo lo pueden hacer los clientes que tengan cuenta en
dólares.
  TRANSFERENCIA_ENVIADA: Solo se puede en pesos y lo que tenga en caja
de ahorro y cuenta corriente debe poder pagar la comisión que se cobra.
  TRANSFERENCIA_RECIBIDA: Sólo en pesos y tener presente que va a estar
rechaza si no estuvo autorizada.
'''