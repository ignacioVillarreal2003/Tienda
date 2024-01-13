from Tarjeta import Tarjeta
from Cliente import Cliente
from Producto import ProductoGenerico, Consumibles, Electronica
from Tienda import Tienda

producto1 = Consumibles("Agua", 40, 10, "Agua mineral de 250ml", "2023-12-12", "2024-01-15")
producto2 = Consumibles("Manzanas", 2.5, 50, "Manzanas frescas", "2023-11-11", "2024-01-29")
producto3 = Consumibles("Yogur", 1.5, 40, "Yogur natural de 200g", "2023-12-20", "2024-01-04")
producto4 = Electronica("Laptop", 899.99, 15, "Laptop ultradelgada con procesador i5", "2024-12-31")
producto5 = Electronica("Cargador portátil", 29.99, 20, "Batería externa de 10000mAh", "2024-09-20")
producto6 = Electronica("Auriculares inalámbricos", 69.99, 10, "Auriculares con cancelación de ruido", "2024-11-11")
producto7 = ProductoGenerico("Camiseta", 19.99, 30, "Camiseta de algodón unisex")
producto8 = ProductoGenerico("Libro", 15, 20, "Bestseller de ciencia ficción")
producto9 = ProductoGenerico("Zapatillas deportivas", 49.99, 25, "Zapatillas para correr")
producto10 = ProductoGenerico("Pelota de fútbol", 19.99, 15, "Pelota oficial de la liga")

tienda1 = Tienda("TATA", "Montevideo", "Comidas y bebidas", "16:00 / 22:00")
tienda1.añadirProducto(producto1)
tienda1.añadirProducto(producto2)
tienda1.añadirProducto(producto3)

tienda2 = Tienda("MACRO", "Montevideo", "Electrodomesticos", "12:00 / 23:30")
tienda2.añadirProducto(producto3)
tienda2.añadirProducto(producto4)
tienda2.añadirProducto(producto5)

targeta1 = Tarjeta(400)
targeta2 = Tarjeta(1000)

cliente1 = Cliente("Pablo", "12345678", targeta1)
cliente2 = Cliente("Chacon", "87654321", targeta2)

tienda1.imprimirProductos()
tienda1.comprarProductos("Agua", 2, cliente1)
tienda1.imprimirProductos()
