import json
from Clases import *
from event_validation import *

def TipoCliente(tipo, tps):
        if tipo=="CLASSIC":
            cliente = ClienteClassic(tps["nombre"], tps["apellido"], tps["numero"], tps["dni"])
        if tipo == "BLACK":
            cliente = ClienteBlack(tps["nombre"], tps["apellido"], tps["numero"], tps["dni"])
        if tipo == "GOLD":
            cliente = ClienteGold(tps["nombre"], tps["apellido"], tps["numero"], tps["dni"])
        return cliente

def TipoTransaccion(transaccion, cliente):
    if transaccion["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
        return cliente.puede_retirar_x_monto(transaccion["monto"], transaccion["saldoEnCuenta"], transaccion["cupoDiarioRestante"])
    if transaccion["tipo"] == "ALTA_CHEQUERA":
        return cliente.puede_tener_chequera(transaccion["totalChequerasActualmente"])
    
    if transaccion["tipo"] == "ALTA_TARJETA_CREDITO":
        return cliente.puede_crear_tarjeta_credito(transaccion["totalTarjetasDeCreditoActualmente"])

    if transaccion["tipo"] == "COMPRA_DOLAR":
        return cliente.tiene_cuenta_dolares(transaccion["monto"], transaccion["saldoEnCuenta"])

    if transaccion["tipo"] == "TRANSFERENCIA_ENVIADA":
        return cliente.puede_hacer_transferencia(transaccion["saldoEnCuenta"], transaccion["monto"])

    if transaccion["tipo"] == "TRANSFERENCIA_RECIBIDA":
        return cliente.puede_recibir_transferencia(transaccion["monto"])


