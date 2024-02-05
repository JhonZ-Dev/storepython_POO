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
