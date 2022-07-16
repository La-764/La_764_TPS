from abc import abstractmethod
from event_validation import Evento
from Clases import *
from transacciones import TransaccionesDet

class Razon:
    @abstractmethod
    def resolver(self,transaccion: TransaccionesDet, evento: Evento):
        pass

    def tipo_cliente(self,evento,transaccion):
        lista_de_cuentas=[]
        if (evento.tipo.lower()=="classic"):
            lista_de_cuentas.append(self.cliente.tiene_cuenta_pesos(transaccion.monto))
            lista_de_cuentas.append(None)
            lista_de_cuentas.append(None)
        if (evento.tipo.lower()=="gold"):
            lista_de_cuentas.append(self.cliente.tiene_cuenta_pesos(transaccion.monto))
            lista_de_cuentas.append(self.cliente.tiene_cuenta_dolares(transaccion.monto))
            lista_de_cuentas.append(self.cliente.tiene_cuenta_corriente(transaccion.monto))
        if(evento.tipo.lower()=="black"):
            lista_de_cuentas.append(self.cliente.tiene_cuenta_pesos(transaccion.monto))
            lista_de_cuentas.append(self.cliente.tiene_cuenta_dolares(transaccion.monto))
            lista_de_cuentas.append(self.cliente.tiene_cuenta_corriente(transaccion.monto))
        
        return lista_de_cuentas
    
    def __init__(self,transaccion,evento):
        self.transaccion = transaccion
        self.evento = evento
        
        if (evento.tipo.lower()=="classic"):
            self.cliente= ClienteClassic(evento)
        if (evento.tipo.lower()=="gold"):
            self.cliente= ClienteGold(evento)
        if(evento.tipo.lower()=="black"):
            self.cliente= ClienteBlack(evento)

        lista_de_cuentas = self.tipo_cliente(evento,transaccion)
        self.caja_ahorro_pesos= lista_de_cuentas[0]
        self.caja_ahorro_dolares= lista_de_cuentas[1]
        self.cuenta_corriente= lista_de_cuentas[2]