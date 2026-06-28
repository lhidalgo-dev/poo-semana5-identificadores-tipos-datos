"""
Modulo: cliente.py
Define la clase Cliente, que representa a una persona registrada
en el sistema del restaurante. Aplica identificadores descriptivos,
tipos de datos basicos y el metodo especial __str__().
"""


class Cliente:
    """Representa a un cliente registrado en el restaurante."""

    # Constructor con identificadores descriptivos y anotaciones de tipo
    def __init__(
        self,
        nombre_completo: str,
        cedula: str,
        edad: int,
        correo_electronico: str,
        es_cliente_frecuente: bool,
    ) -> None:
        self.nombre_completo = nombre_completo            # str -> nombre y apellido del cliente
        self.cedula = cedula                              # str -> identificacion (texto, no se opera)
        self.edad = edad                                  # int -> edad en anios
        self.correo_electronico = correo_electronico      # str -> correo de contacto
        self.es_cliente_frecuente = es_cliente_frecuente  # bool -> indica si es cliente habitual

    # Metodo especial para representar el objeto como texto legible
    def __str__(self) -> str:
        tipo_cliente = "Frecuente" if self.es_cliente_frecuente else "Ocasional"
        return (
            f"{self.nombre_completo} | C.I.: {self.cedula} | "
            f"Edad: {self.edad} | Correo: {self.correo_electronico} | {tipo_cliente}"
        )
