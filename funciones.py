import json
from Clases import *
from event_validation import *

def TipoCliente(tipo, tps):
        if tipo=="CLASSIC":
            cliente = ClienteClassic(tps["nombre"], tps["apellido"], tps["dni"], tps["transacciones"])
        if tipo == "BLACK":
            cliente = ClienteBlack(tps["nombre"], tps["apellido"], tps["dni"], tps["transacciones"])
        if tipo == "GOLD":
            cliente = ClienteGold(tps["nombre"], tps["apellido"], tps["dni"], tps["transacciones"])
        return cliente
 



