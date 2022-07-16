import json
from Clases import *
from event_validation import *
from razon_de_rechazo import Razon
from transacciones import TransaccionesDet

class razon_compra_dolar(Razon):
    def resolver(self):
        if self.cliente.puede_comprar_dolar() == False:
            return 'Posee una cuenta que no puede comprar dolares'
        
        if self.transaccion.monto > self.transaccion.saldoEnCuenta:
            return 'No dispone de saldo suficiente para la compra de dolares'

class razon_retiro_efectivo(Razon):
    def resolver(self):
        if  self.transaccion.monto < self.transaccion.cupoDiarioRestante:
            if self.transaccion.monto < self.transaccion.saldoEnCuenta:
                pass
            else:
                return 'Saldo insuficiente'
        else:
            return f'Superaste el cupo diario de retiro de efectivo dispuesto para su tipo de cuenta' 

class razon_alta_chequera(Razon):
    def resolver(self):
        if self.cliente.puede_tener_chequera() == False:
            return 'El cliente no puede crear chequera'
        else:
            max = self.cliente.max_chequera()
            if ( max <= self.transaccion.totalChequerasActualmente):
                return 'Se supera la maxima cantidad de chequeras dispuesta para su tipo de cuenta'

class razon_alta_tarjeta_credito(Razon):
    def resolver(self):
        if self.cliente.puede_crear_tarjeta_credito() == False:
            return 'El cliente no puede crear tarjeta de credito'
        else:
            cantidad_disponible = self.cliente.max_tarjeta_credito()
            if ( cantidad_disponible <= self.transaccion.totalTarjetasDeCreditoActualmente):
                return 'Se supera la cantidad de tarjetas de credito dispuesta para su tipo de cuenta'

class razon_transferencia_recibida(Razon):
    def resolver(self):
        if (self.evento.tipo.lower() == 'classic' or self.evento.tipo.lower() == 'gold'):
            if self.transaccion.monto > self.caja_ahorro_pesos.limite_transferencia_recibida:
                if self.evento.tipo.lower() == 'classic':
                    return f'La transferencia a recibir supera los ${self.caja_ahorro_pesos.limite_transferencia_recibida} que es tu limite de extracción a recibir'
                else:
                    return f'Las transferencias a recibir que supera los ${self.caja_ahorro_pesos.limite_transferencia_recibida} deben ser autorizadas previamente'