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
    def calcular_total(self):
        return sum(producto.precio for producto in self.productos)
def agregar_producto():
    tipo_producto = input("Ingrese el tipo de producto (E para electrónico, cualquier otra tecla para estándar): ").upper()
    id_producto = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock inicial del producto: "))
    if tipo_producto == 'E':
        garantia_meses = int(input("Ingrese la garantía en meses: "))
        producto = ProductoElectronico(id_producto, nombre, precio, stock, garantia_meses)
    else:
        producto = Producto(id_producto, nombre, precio, stock)

    productos.append(producto)
    print("Producto agregado con éxito.")

def listar_productos():
    print("Lista de productos:")
    for producto in productos:
        print(producto.mostrar_informacion())
def realizar_venta():
    id_cliente = input("Ingrese el ID del cliente: ")
    cliente = buscar_cliente(id_cliente)

     if cliente:
        productos_venta = []
        while True:
            listar_productos()
            id_producto = input("Ingrese el ID del producto a vender (0 para finalizar): ")
            if id_producto == '0':
                break
            producto = buscar_producto(id_producto)
            if producto and producto.stock > 0:
                productos_venta.append(producto)
                producto.stock -= 1
            else:
                print("Producto no encontrado o sin stock disponible.")
        if productos_venta:
            id_venta = len(ventas) + 1
            venta = Venta(id_venta, cliente, productos_venta)
            ventas.append(venta)
            print("Venta realizada con éxito.")
            print(f"Total de la venta: ${venta.calcular_total()}")
        else:
            print("No se realizaron ventas.")
     else:
        print("Cliente no encontrado.")
def buscar_cliente(id_cliente):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            return cliente
    return None
def buscar_producto(id_producto):
    for producto in productos:
        if producto.id_producto == id_producto:
            return producto
    return None
# Inicialización de datos
productos = [
    Producto("P001", "Camiseta", 20.0, 50),
    Producto("P002", "Pantalón", 30.0, 30),
    ProductoElectronico("PE001", "Laptop", 800.0, 10, 12),
    Producto("P003", "Zapatos", 50.0, 20)
]
clientes = [
    Cliente("C001", "Juan Pérez", "Calle 123", "juan@gmail.com"),
    Cliente("C002", "María López", "Avenida 456", "maria@gmail.com"),
    Cliente("C003", "Carlos Rodríguez", "Plaza Principal", "carlos@gmail.com")
]
ventas = []
# Menú principal
while True:
    print("\nSistema de Tienda")
    print("1. Agregar Producto")
    print("2. Listar Productos")
    print("3. Realizar Venta")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        listar_productos()
    elif opcion == '3':
        realizar_venta()
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")




