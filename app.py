from event_validation import *
from Clases import *
from funciones import *
from transacciones import TransaccionesDet
import datos_output
import csv

def concatPath(nombreJSON):
    directory = 'test_event/'
    nombreJSON = directory + nombreJSON
    return nombreJSON
def main():
    rechazo = []
    nombreJSON = input("Ingrese el nombre del archivo: ")
    nombreHTML= input("Ingrese el nombre del archivo de salida HTML: ")
    tps = Evento()
    nombreJSON=concatPath(nombreJSON)
    tps.leerJSON(nombreJSON)
    cliente= Cliente(tps)
    for t in tps.transacciones:
        if t.estado == "RECHAZADA":
            match t.tipo.lower():
                case 'transferencia_enviada':
                    razon=(razon_transferencia_enviada(t,tps).resolver())
                    rechazo.append(razon)
                case 'transferencia_recibida':
                   razon=(razon_transferencia_recibida(t,tps).resolver())
                   rechazo.append(razon)
                case 'alta_tarjeta_credito':
                    razon=(razon_alta_tarjeta_credito(t,tps).resolver())
                    rechazo.append(razon)
                case 'alta_chequera':
                    razon=(razon_alta_chequera(t,tps).resolver())
                    rechazo.append(razon)
                case 'compra_dolar':
                    razon=(razon_compra_dolar(t,tps).resolver())
                    rechazo.append(razon)
                case'retiro_efectivo_cajero_automatico':
                    razon=(razon_retiro_efectivo(t,tps).resolver())
                    rechazo.append(razon)
        else:
            razon=(aceptada(t,tps).resolver())
            rechazo.append(razon)
    print(rechazo)    
main()