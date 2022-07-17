import string
class DireccionDesc:
    calle=string
    ciudad=string
    provincia=string
    pais=string

    def __init__(self, dt) -> None:
        self.calle=dt['calle']
        self.numero=dt['numero']
        self.ciudad=dt['ciudad']
        self.provincia=dt['provincia']
        self.pais=dt['pais']
    def __str__(self):
        return f"{self.calle} {self.numero}, {self.ciudad}, {self.provincia}, {self.pais}"