class Cuenta:
    def __init__(self, monto, limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible):
        self.__monto = monto
        self.__limite_extraccion_diario = limite_extraccion_diario
        self.__limite_transferencia_recibida = limite_transferencia_recibida
        self.__costo_transferencias = costo_transferencias
        self.__saldo_descubierto_disponible = saldo_descubierto_disponible

    def get_monto(self):
        return self.__monto

    def set_monto(self, monto):
        try:
            floatMonto = float(monto)
            self.__monto = floatMonto
        except ValueError:
            raise ValueError("El monto debe ser un numero o poder ser convertido en un numero")
        except TypeError:
            raise TypeError("El monto debe ser un numero o poder ser convertido en un numero")
        except:
            raise
        finally:
            return "Monto: " + str(self.__monto)

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
            self.__monto = floatSaldoDescubiertoDisponible
        except ValueError:
            raise ValueError("El saldo descubierto disponible debe ser un numero o poder ser convertido en un numero")
        except TypeError:
            raise TypeError("El saldo descubierto disponible debe ser un numero o poder ser convertido en un numero")
        except:
            raise
        finally:
            return "Saldo descubierto disponible: " + str(self.__saldo_descubierto_disponible)