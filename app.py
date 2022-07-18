from event_validation import *
from Clases import *
from funciones import *
from transacciones import TransaccionesDet
import csv
from reporte import *

def obtenerRazon(t,tps):
            if t.estado == "RECHAZADA":
                match t.tipo.lower():
                    case 'transferencia_enviada':
                        return (razon_transferencia_enviada(t,tps).resolver())
                    case 'transferencia_recibida':
                        return (razon_transferencia_recibida(t,tps).resolver())
                    case 'alta_tarjeta_credito':
                        return (razon_alta_tarjeta_credito(t,tps).resolver())
                    case 'alta_chequera':
                        return (razon_alta_chequera(t,tps).resolver())
                    case 'compra_dolar':
                        return (razon_compra_dolar(t,tps).resolver())
                    case'retiro_efectivo_cajero_automatico':
                        return (razon_retiro_efectivo(t,tps).resolver())
            else:
                return (aceptada(t,tps).resolver())
                


def concatPath(nombreJSON):
    directory = 'test_event/'
    nombreJSON = directory + nombreJSON
    return nombreJSON
def main():
    resultados = []
    nombreJSON = input("Ingrese el nombre del archivo: ")
    tps = Evento()
    nombreJSON=concatPath(nombreJSON)
    tps.leerJSON(nombreJSON)
    cliente= Cliente(tps)
    for t in tps.transacciones:
        resultado = t
        resultado.razon = ((obtenerRazon(t,tps)))
        resultados.append(resultado)
    CreadorHTML(cliente, resultados,tps) 
main()