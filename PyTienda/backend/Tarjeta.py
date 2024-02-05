import random
from backend.util import Comprobaciones


class Tarjeta:
    def __init__(self, monto: float):
        self.numeroTarjeta: int = random.randint(100000, 999999)
        if Comprobaciones.noNegativo(monto):
            self.monto: float = monto
        else:
            raise ValueError("El monto no puede ser negativo.")

    def getNumeroTarjeta(self) -> int:
        return self.numeroTarjeta

    def getMonto(self) -> float:
        return self.monto

    def setMonto(self, montoNuevo: float) -> None:
        if Comprobaciones.noNegativo(montoNuevo):
            self.monto = montoNuevo
        else:
            raise ValueError("El monto no puede ser negativo.")
