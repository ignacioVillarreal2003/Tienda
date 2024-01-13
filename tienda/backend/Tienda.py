from datetime import datetime
from typing import Dict

from Producto import ProductoGenerico
from Cliente import Cliente
from backend.util import Comprobaciones


class Tienda:
    def __init__(self, nombre: str, ubicacion: str, tipo: str, horario: str):
        if Comprobaciones.noVacio(nombre):
            self.nombre: str = nombre
        else:
            raise ValueError("El nombre no puede ser vacio.")
        self.ubicacion: str = ubicacion
        self.tipo: str = tipo
        self.horario: str = horario
        self.productos: Dict[str, ProductoGenerico] = {}

    def getNombre(self) -> str:
        return self.nombre

    def getUbicacion(self) -> str:
        return self.ubicacion

    def getTipo(self) -> str:
        return self.tipo

    def getHorario(self) -> str:
        return self.horario

    def getProductos(self) -> Dict[str, ProductoGenerico]:
        return self.productos

    def setNombre(self, nombreNuevo: str) -> None:
        if Comprobaciones.noVacio(nombreNuevo):
            self.nombre: str = nombreNuevo
        else:
            raise ValueError("El nombre no puede ser vacio.")

    def setUbicacion(self, ubicacionNueva: str) -> None:
        self.ubicacion = ubicacionNueva

    def setTipo(self, tipoNuevo: str) -> None:
        self.tipo = tipoNuevo

    def setHorario(self, horarioNuevo: str) -> None:
        self.horario = horarioNuevo

    def añadirProducto(self, producto: ProductoGenerico) -> ProductoGenerico:
        self.productos[producto.nombre] = producto
        return producto

    def eliminarProducto(self, nombreProducto: str) -> None:
        self.productos.pop(nombreProducto)

    def actualizarProducto(self, nombreProducto: str, precioNuevo: float = None, stockNuevo: int = None, descripcionNueva: str = None) -> ProductoGenerico:
        producto = self.productos[nombreProducto]
        if precioNuevo is not None:
            producto.setPrecio(precioNuevo)
        if stockNuevo is not None:
            producto.setStock(stockNuevo)
        if descripcionNueva is not None:
            producto.setDescripcion(descripcionNueva)
        return producto

    def imprimirTienda(self) -> None:
        print(f"{self.nombre} - {self.ubicacion} - {self.tipo} - {self.horario}")

    def imprimirProductos(self) -> None:
        format_string = "{:<20} {:<8} {:<8} {:<30}"
        print("--------------------------- Productos ---------------------------")
        print(format_string.format("Nombre", "Precio", "Stock", "Descripción"))
        for nombreProducto in self.productos.keys():
            producto = self.productos[nombreProducto]
            print(format_string.format(
                nombreProducto,
                producto.getPrecio(),
                producto.getStock(),
                producto.getDescripcion()
            ))
        print("-----------------------------------------------------------------")


    def comprarProductos(self, nombreProducto: str, cantidad: int, cliente: Cliente) -> None:
        producto = self.productos[nombreProducto]
        precio_total = producto.getPrecio() * cantidad

        if cliente.getTarjeta().getMonto() >= precio_total:
            producto.setStock(producto.getStock() - cantidad)
            cliente.getTarjeta().setMonto(cliente.getTarjeta().getMonto() - precio_total)
            print(self.getBoleta(producto, cantidad, precio_total, cliente))
        else:
            print("No tiene saldo suficiente en la tarjeta.")

    def getBoleta(self, producto: ProductoGenerico, cantidad: int, precio_total: float, cliente: Cliente) -> str:
        boleta = ""
        boleta += "---------- Boleta de Compra ----------\n"
        boleta += f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        boleta += f"Cliente: {cliente.getNombre()}\n"
        boleta += f"Producto: {producto.getNombre()}\n"
        boleta += f"Cantidad: {cantidad}\n"
        boleta += f"Precio unitario: {producto.getPrecio()}\n"
        boleta += f"Precio total: {precio_total}\n"
        boleta += f"Monto restante en la tarjeta: {cliente.getTarjeta().getMonto()}\n"
        boleta += "--------------------------------------"
        return boleta
