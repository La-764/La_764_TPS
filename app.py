from event_validation import *
from Clases import *
from funciones import *

def main():
    
    rechazo = []
    nombreJSON = input("Ingrese el nombre del archivo: ")
    tps = leerJSON(nombreJSON)
    cliente = TipoCliente(tps["tipo"] ,tps)
    print(cliente)
    #for transaccion in cliente.transacciones:
        #if transaccion["estado"] == "RECHAZADA":
            #rechazo.append(TipoTransaccion(transaccion, cliente))
        #else:
            #rechazo.append("-")

    #print(rechazo)
   
   
main()