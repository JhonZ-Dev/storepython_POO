class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def mostrar_informacion(self):
        return f"{self.nombre} - Precio: ${self.precio} - Stock: {self.stock}"