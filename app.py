from event_validation import *
from Clases import *
from funciones import *
from transacciones import TransaccionesDet

def main():
    
    rechazo = []
    nombreJSON = input("Ingrese el nombre del archivo: ")
    tps = leerJSON(nombreJSON)
    cliente= Cliente(tps)
    for t in tps.transacciones:
        if t.estado == "RECHAZADA":
            match t.tipo.lower():
                case 'transferencia_enviada':
                    print(RazonTransferenciaEnviada(t,tps).resolver()) #en vez de print va return para mandar los datos a una variable
                case 'transferencia_recibida':
                    print(RazonTransferenciaRecibida(t,tps).resolver())
                case 'alta_tarjeta_credito':
                    print(RazonAltaTarjetaCredito(t,tps).resolver())
                case 'alta_chequera':
                    print(RazonAltaChequera(t,tps).resolver())
                case 'comprar_dolar':
                    print(RazonCompraDolar(t,tps).resolver())
                case'retiro_efectivo_cajero_automatico':
                    print(RazonRetiroEfectivo(t,tps).resolver())

   
   
main()