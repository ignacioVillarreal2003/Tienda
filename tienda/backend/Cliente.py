from Tarjeta import *
from backend.util import Comprobaciones


class Cliente:
    def __init__(self, nombre: str, ci: str, tarjeta: Tarjeta):
        if Comprobaciones.noVacio(nombre) & Comprobaciones.noNumeros(nombre):
            self.nombre: str = nombre
        else:
            raise ValueError("El nombre no puede ser vacio, ni contener numeros.")
        if Comprobaciones.comprobarCedula(ci):
            self.ci: str = ci
        else:
            raise ValueError("La cédula debe tener exactamente 8 caracteres.")
        self.tarjeta: Tarjeta = tarjeta

    def getNombre(self) -> str:
        return self.nombre

    def getCi(self) -> str:
        return self.ci

    def getTarjeta(self) -> Tarjeta:
        return self.tarjeta

    def setNombre(self, nombreNuevo: str) -> None:
        if Comprobaciones.noVacio(nombreNuevo) & Comprobaciones.noNumeros(nombreNuevo):
            self.nombre = nombreNuevo
        else:
            raise ValueError("El nombre no puede ser vacio, ni contener numeros.")

    def setCi(self, ciNueva: str) -> None:
        if Comprobaciones.comprobarCedula(ciNueva):
            self.ci = ciNueva
        else:
            raise ValueError("La cédula debe tener exactamente 8 caracteres.")

    def setTarjeta(self, tarjetaNueva: Tarjeta) -> None:
        self.tarjeta = tarjetaNueva
