from event_validation import *
from Clases import *
from funciones import *
from transacciones import TransaccionesDet

def main():
    rechazo = []
    nombreJSON = input("Ingrese el nombre del archivo: ")
    tps = Evento()
    tps.leerJSON(nombreJSON)
    cliente= Cliente(tps)
    for t in tps.transacciones:
        if t.estado == "RECHAZADA":
            match t.tipo.lower():
                case 'transferencia_enviada':
                    print(razon_transferencia_enviada(t,tps).resolver()) #en vez de print va return para mandar los datos a una variable
                case 'transferencia_recibida':
                    print(razon_transferencia_recibida(t,tps).resolver())
                case 'alta_tarjeta_credito':
                    print(razon_alta_tarjeta_credito(t,tps).resolver())
                case 'alta_chequera':
                    print(razon_alta_chequera(t,tps).resolver())
                case 'compra_dolar':
                    print(razon_compra_dolar(t,tps).resolver())
                case'retiro_efectivo_cajero_automatico':
                    print(razon_retiro_efectivo(t,tps).resolver())

   
   
main()