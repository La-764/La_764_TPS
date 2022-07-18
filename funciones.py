import json
from Clases import *
from event_validation import *
from razon_de_rechazo import Razon
from transacciones import TransaccionesDet

class aceptada(Razon):
    def resolver(self):
        return "Aceptada"

class razon_compra_dolar(Razon):
    def resolver(self):
        if self.cliente.puede_comprar_dolar() == False:
            return 'Posee una cuenta que no puede comprar dolares'
        
        if self.transaccion.monto > self.transaccion.saldoEnCuenta:
            return 'No dispone de saldo suficiente para la compra de dólares'

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
                return 'Se supera la máxima cantidad de chequeras dispuesta para su tipo de cuenta'

class razon_alta_tarjeta_credito(Razon):
    def resolver(self):
        if self.cliente.puede_crear_tarjeta_credito() == False:
            return 'El cliente no puede crear tarjeta de crédito'
        else:
            cantidad_disponible = self.cliente.max_tarjeta_credito()
            if ( cantidad_disponible <= self.transaccion.totalTarjetasDeCreditoActualmente):
                return 'Se supera la cantidad de tarjetas de credito dispuesta para su tipo de cuenta'

class razon_transferencia_recibida(Razon):
    def resolver(self):
        if (self.evento.tipo.lower() == 'classic' or self.evento.tipo.lower() == 'gold'):
            if self.transaccion.monto > self.caja_ahorro_pesos.limite_transferencia_recibida:
                if self.evento.tipo.lower() == 'classic':
                    return f'La transferencia a recibir supera los ${self.caja_ahorro_pesos.limite_transferencia_recibida} que es tu limite de extracción a recibir dispuesto para su tipo de cuenta'
                else:
                    return f'Las transferencias a recibir que supera los ${self.caja_ahorro_pesos.limite_transferencia_recibida} deben ser autorizadas previamente'

class razon_transferencia_enviada(Razon):
    def resolver(self):      
        costo_trans= self.caja_ahorro_pesos.monto + self.caja_ahorro_pesos.costo_transferencias

        if self.cuenta_corriente == None:
            if costo_trans < self.caja_ahorro_pesos.limite_extraccion_diario:
                if self.transaccion.saldoEnCuenta > costo_trans:
                    pass
                else:
                    return 'Estás intentando transferir más plata de lo disponible actualmente'
            else:
                return f'La transferencia a realizar supera tu límite de extracción diario'
        else: 
            if costo_trans < self.caja_ahorro_pesos.limite_extraccion_diario:
                if self.transaccion.saldoEnCuenta > costo_trans:
                    pass
                else:
                    if (self.transaccion.saldoEnCuenta - costo_trans < -1*(self.cuenta_corriente.saldo_descubierto_disponible)):
                        return f'El descubierto definido para su tipo de cuenta no puede cubrir la transferencia'
            else:
                return f'La transferencia superan los que es tu límite de extracción diario'