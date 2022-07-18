class TransaccionesDet:
    def __init__(self, data):
        self.estado=data['estado']
        self.tipo=data['tipo']
        self.cuentaNumero=data['cuentaNumero']
        self.cupoDiarioRestante=data['cupoDiarioRestante']
        self.monto=data['monto']
        self.fecha=data['fecha']
        self.numero=data['numero']
        self.saldoEnCuenta=data['saldoEnCuenta']
        self.totalTarjetasDeCreditoActualmente=data['totalTarjetasDeCreditoActualmente']
        self.totalChequerasActualmente=data['totalChequerasActualmente']
    def __str__(self):
        return f"{self.fecha} {self.tipo}, {self.estado}, {self.monto}"
