"""
Modulo: producto.py
Define la clase Producto, que representa un plato, bebida o producto
disponible en el restaurante. Aplica identificadores descriptivos,
tipos de datos basicos y el metodo especial __str__().
"""


class Producto:
    """Representa un producto del menu del restaurante."""

    # Constructor con identificadores descriptivos y anotaciones de tipo
    def __init__(
        self,
        nombre: str,
        categoria: str,
        precio: float,
        cantidad_disponible: int,
        esta_disponible: bool,
    ) -> None:
        self.nombre = nombre                              # str  -> nombre del producto
        self.categoria = categoria                        # str  -> tipo (plato, bebida, postre)
        self.precio = precio                              # float -> precio unitario
        self.cantidad_disponible = cantidad_disponible    # int  -> unidades en stock
        self.esta_disponible = esta_disponible            # bool -> indica si se puede vender

    # Metodo que reduce el stock y actualiza el estado del producto
    def reducir_stock(self, cantidad_vendida: int) -> None:
        if 0 < cantidad_vendida <= self.cantidad_disponible:
            self.cantidad_disponible -= cantidad_vendida
        if self.cantidad_disponible == 0:
            self.esta_disponible = False

    # Metodo especial para representar el objeto como texto legible
    def __str__(self) -> str:
        estado = "Disponible" if self.esta_disponible else "Agotado"
        return (
            f"{self.nombre} ({self.categoria}) - "
            f"${self.precio:.2f} | Stock: {self.cantidad_disponible} | {estado}"
        )
