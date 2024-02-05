import tkinter as tk
from backend.Producto import ProductoGenerico, Consumibles, Electronica
from backend.Tienda import Tienda
from backend.Cliente import Cliente
from backend.Tarjeta import Tarjeta

cliente = None
tarjeta = None
class MainVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Tienda Online")
        self.root.geometry("500x300")
        self.label_descripcion = tk.Label(text="Ingresar")
        self.btn_usuario = tk.Button(root, text="Usuario", command=self.ventana_usuario)
        self.btn_admin = tk.Button(root, text="Admin", command=self.ventana_admin)

        self.label_descripcion.pack()
        self.btn_usuario.pack()
        self.btn_admin.pack()

    def ventana_usuario(self):
        self.root.destroy()
        siguiente_ventana = tk.Tk()
        SeleccionUsuarioVentana(siguiente_ventana)

    def ventana_admin(self):
        self.root.destroy()
        siguiente_ventana = tk.Tk()
        #VentanaPrincipal(siguiente_ventana)

class SeleccionUsuarioVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Tienda Online")
        self.root.geometry("500x300")
        self.label_descripcion = tk.Label(text="Seleccione una opcion")
        self.btn_registrar_usuario = tk.Button(root, text="Registrar usuario", command=self.ventana_registrar_usuario)
        self.btn_loguear_admin = tk.Button(root, text="Loguear usuario", command=self.ventana_loguear_usuario)
        self.label_descripcion.pack()
        self.btn_registrar_usuario.pack()
        self.btn_loguear_admin.pack()

    def ventana_registrar_usuario(self):
        self.root.destroy()
        siguiente_ventana = tk.Tk()
        RegistrarUsuarioVentana(siguiente_ventana)

    def ventana_loguear_usuario(self):
        self.root.destroy()
        siguiente_ventana = tk.Tk()
        InicioSesionUsuarioVentana(siguiente_ventana)


class InicioSesionUsuarioVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Tienda Online")
        self.root.geometry("500x300")
        self.label_usuario = tk.Label(root, text="Usuario:")
        self.entry_usuario = tk.Entry(root)
        self.boton_iniciar_sesion = tk.Button(root, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.label_usuario.pack()
        self.entry_usuario.pack()
        self.boton_iniciar_sesion.pack()
    def iniciar_sesion(self):
        self.root.destroy()
        siguiente_ventana = tk.Tk()
        #VentanaPrincipal(siguiente_ventana)

class IngresarDatosInicioSesionVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Tienda Online")
        self.root.geometry("500x300")
        self.label_nombre = tk.Label(root, text="Nombre:")
        self.entry_nombre = tk.Entry(root)
        self.boton_registrar = tk.Button(root, text="Iniciar", command=self.iniciar_sesion)
        self.label_nombre.pack()
        self.entry_nombre.pack()
        self.boton_registrar.pack()

    def iniciar_sesion(self):
        global tarjeta
        global cliente
        # Obtener cliente de la bd
        targetaNueva = Tarjeta(1000)
        clienteNuevo = Cliente(self.entry_nombre.get(), self.entry_cedula.get(), targetaNueva)
        tarjeta = targetaNueva
        cliente = clienteNuevo
        self.root.destroy()
        siguiente_ventana = tk.Tk()
        VistaUsuarioVentana(siguiente_ventana)
class RegistrarUsuarioVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Tienda Online")
        self.root.geometry("500x300")
        self.label_usuario = tk.Label(root, text="Usuario:")
        self.entry_usuario = tk.Entry(root)
        self.boton_registrar = tk.Button(root, text="Registrar", command=self.registrar)
        self.label_usuario.pack()
        self.entry_usuario.pack()
        self.boton_registrar.pack()

    def registrar(self):
        self.root.destroy()  # Cerrar la ventana actual
        siguiente_ventana = tk.Tk()
        IngresarDatosRegistroVentana(siguiente_ventana)

class IngresarDatosRegistroVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Tienda Online")
        self.root.geometry("500x300")
        self.label_nombre = tk.Label(root, text="Nombre:")
        self.entry_nombre = tk.Entry(root)
        self.label_cedula = tk.Label(root, text="Cedula:")
        self.entry_cedula = tk.Entry(root)
        self.boton_registrar = tk.Button(root, text="Registrar", command=self.registrar)
        self.label_nombre.pack()
        self.entry_nombre.pack()
        self.label_cedula.pack()
        self.entry_cedula.pack()
        self.boton_registrar.pack()

    def registrar(self):
        global tarjeta
        global cliente
        targetaNueva = Tarjeta(1000)
        clienteNuevo = Cliente(self.entry_nombre.get(), self.entry_cedula.get(), targetaNueva)
        tarjeta = targetaNueva
        cliente = clienteNuevo
        # Guardar en bd
        self.root.destroy()
        siguiente_ventana = tk.Tk()
        VistaUsuarioVentana(siguiente_ventana)

class VistaUsuarioVentana:
    def __init__(self):
        self.root = tk.Tk()


root = tk.Tk()
root.title("Tienda Online")
root.geometry("500x300")
inicio_sesion_ventana = MainVentana(root)
root.mainloop()




