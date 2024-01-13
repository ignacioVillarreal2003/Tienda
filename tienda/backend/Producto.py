from datetime import datetime
from backend.util import Comprobaciones


class ProductoGenerico:
    def __init__(self, nombre: str, precio: float, stock: int, descripcion: str):
        if Comprobaciones.noVacio(nombre):
            self.nombre: str = nombre
        else:
            raise ValueError("El nombre no puede ser vacio.")
        if Comprobaciones.noNegativo(precio):
            self.precio: float = precio
        else:
            raise ValueError("El precio no puede ser menor a 0.")
        if Comprobaciones.noNegativo(stock):
            self.stock: int = stock
        else:
            raise ValueError("El stock no puede ser menor a 0.")
        self.descripcion: str = descripcion

    def getNombre(self) -> str:
        return self.nombre

    def getPrecio(self) -> float:
        return self.precio

    def getStock(self) -> int:
        return self.stock

    def getDescripcion(self) -> str:
        return self.descripcion

    def setNombre(self, nombreNuevo: str) -> None:
        if Comprobaciones.noVacio(nombreNuevo) & Comprobaciones.noNumeros(nombreNuevo):
            self.nombre = nombreNuevo
        else:
            raise ValueError("El nombre no puede ser vacio, ni contener numeros.")

    def setPrecio(self, precioNuevo: float) -> None:
        if Comprobaciones.noNegativo(precioNuevo):
            self.precio = precioNuevo
        else:
            raise ValueError("El precio no puede ser menor a 0.")

    def setStock(self, stockNuevo: int) -> None:
        if Comprobaciones.noNegativo(stockNuevo):
            self.stock = stockNuevo
        else:
            raise ValueError("El stock no puede ser menor a 0.")

    def setDescripcion(self, descripcionNueva: str) -> None:
        self.descripcion = descripcionNueva


class Consumibles(ProductoGenerico):
    def __init__(self, nombre: str, precio: float, stock: int, descripcion: str, fechaElaboracion: datetime, fechaVencimiento: datetime):
        super().__init__(nombre, precio, stock, descripcion)
        self.fechaElaboracion: datetime = fechaElaboracion
        self.fechaVencimiento: datetime = fechaVencimiento

    def getFechaElaboracion(self) -> datetime:
        return self.fechaElaboracion

    def setFechaElaboracion(self, fechaElaboracionNueva: datetime) -> None:
        self.fechaElaboracion = fechaElaboracionNueva

    def getFechaVencimiento(self) -> datetime:
        return self.fechaVencimiento

    def setFechaVencimiento(self, fechaVencimientoNueva: datetime) -> None:
        self.fechaVencimiento = fechaVencimientoNueva


class Electronica(ProductoGenerico):
    def __init__(self, nombre: str, precio: float, stock: int, descripcion: str, fechaGarantia: datetime):
        super().__init__(nombre, precio, stock, descripcion)
        self.fechaGarantia: datetime = fechaGarantia

    def getFechaGarantia(self) -> datetime:
        return self.fechaGarantia

    def setFechaGarantia(self, fechaGarantiaNueva: datetime) -> None:
        self.fechaGarantia = fechaGarantiaNueva
