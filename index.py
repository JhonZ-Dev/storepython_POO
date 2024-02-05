class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def mostrar_informacion(self):
        return f"{self.nombre} - Precio: ${self.precio} - Stock: {self.stock}"

class ProductoElectronico(Producto):
    def __init__(self, id_producto, nombre, precio, stock, garantia_meses):
        super().__init__(id_producto, nombre, precio, stock)
        self.garantia_meses = garantia_meses
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} - Garantía: {self.garantia_meses} meses"

class Cliente:
    def __init__(self, id_cliente, nombre, direccion, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
class Venta:
    def __init__(self, id_venta, cliente, productos):
        self.id_venta = id_venta
        self.cliente = cliente
        self.productos = productos