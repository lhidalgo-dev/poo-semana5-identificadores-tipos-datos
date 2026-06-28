"""
Modulo: restaurante.py
Define la clase Restaurante, servicio principal que administra
las listas de productos y clientes registrados en el sistema.
Utiliza listas como tipo de dato compuesto e importaciones de los modelos.
"""

# Importaciones de los modelos definidos en el paquete "modelos"
from modelos import Producto, Cliente


class Restaurante:
    """Servicio que gestiona los productos y clientes del restaurante."""

    def __init__(self, nombre_restaurante: str) -> None:
        self.nombre_restaurante = nombre_restaurante      # str -> nombre del restaurante
        # Listas como tipo de dato compuesto para almacenar varios objetos
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []

    # Agrega un objeto Producto a la lista de productos
    def agregar_producto(self, producto: Producto) -> None:
        self.lista_productos.append(producto)

    # Agrega un objeto Cliente a la lista de clientes
    def agregar_cliente(self, cliente: Cliente) -> None:
        self.lista_clientes.append(cliente)

    # Recorre la lista y cuenta cuantos productos estan disponibles
    def contar_productos_disponibles(self) -> int:
        productos_activos = 0
        for producto in self.lista_productos:
            if producto.esta_disponible:
                productos_activos += 1
        return productos_activos

    # Muestra en consola todos los productos registrados
    def mostrar_productos(self) -> None:
        print(f"--- Menu de {self.nombre_restaurante} ---")
        for producto in self.lista_productos:
            print(f"  - {producto}")

    # Muestra en consola todos los clientes registrados
    def mostrar_clientes(self) -> None:
        print(f"--- Clientes registrados en {self.nombre_restaurante} ---")
        for cliente in self.lista_clientes:
            print(f"  - {cliente}")

    # Metodo especial para representar el servicio como texto legible
    def __str__(self) -> str:
        return (
            f"Restaurante {self.nombre_restaurante} | "
            f"Productos registrados: {len(self.lista_productos)} | "
            f"Clientes registrados: {len(self.lista_clientes)}"
        )
