"""
Archivo: main.py
Punto de arranque del sistema de gestion del restaurante.
Aqui se crean los objetos, se agregan al servicio principal
y se muestra la informacion registrada de forma organizada en consola.
"""

# Importaciones de las clases del proyecto (uso correcto de paquetes)
from modelos import Producto, Cliente
from servicios import Restaurante


def main() -> None:
    # Se crea el objeto principal del servicio (clase Restaurante)
    mi_restaurante = Restaurante("El Sabor Andino")

    # Creacion de varios objetos del modelo Producto
    producto_uno = Producto("Lomo Saltado", "Plato fuerte", 8.50, 20, True)
    producto_dos = Producto("Jugo de Mora", "Bebida", 2.25, 15, True)
    producto_tres = Producto("Cheesecake", "Postre", 3.75, 0, False)

    # Creacion de varios objetos del modelo Cliente
    cliente_uno = Cliente("Ana Maria Perez", "0102030405", 28, "ana.perez@correo.com", True)
    cliente_dos = Cliente("Carlos Ramirez", "0605040302", 35, "carlos.ramirez@correo.com", False)

    # Se agregan los productos a la lista del servicio principal
    mi_restaurante.agregar_producto(producto_uno)
    mi_restaurante.agregar_producto(producto_dos)
    mi_restaurante.agregar_producto(producto_tres)

    # Se agregan los clientes a la lista del servicio principal
    mi_restaurante.agregar_cliente(cliente_uno)
    mi_restaurante.agregar_cliente(cliente_dos)

    # Se muestra la informacion registrada de forma organizada en consola
    print("===================================================")
    print(f" SISTEMA DE GESTION: {mi_restaurante.nombre_restaurante}")
    print("===================================================")
    print()

    mi_restaurante.mostrar_productos()
    print()
    mi_restaurante.mostrar_clientes()
    print()

    # Uso de un metodo que devuelve un valor calculado (int)
    productos_disponibles = mi_restaurante.contar_productos_disponibles()
    print(f"Productos disponibles actualmente: {productos_disponibles}")
    print(f"Resumen general -> {mi_restaurante}")


# Punto de arranque del programa
if __name__ == "__main__":
    main()
