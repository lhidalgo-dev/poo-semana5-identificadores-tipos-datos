# Sistema de Gestión de Restaurante — Semana 5 (POO)

- **Estudiante:** Leython Josue Hidalgo Valdez
- **Asignatura:** Programación Orientada a Objetos
- **Tema:** Aplicación de identificadores y tipos de datos en un proyecto Python modular

---

## Descripción del sistema

Este proyecto es un sistema básico de gestión de restaurante desarrollado con **Programación Orientada a Objetos en Python**. Su objetivo es demostrar el uso correcto de identificadores descriptivos, tipos de datos básicos, clases, objetos, constructores, métodos, el método especial `__str__()`, importaciones entre módulos y listas como tipo de dato compuesto.

El sistema permite registrar **productos** (platos, bebidas o postres) y **clientes** del restaurante, almacenarlos en listas dentro de un servicio principal y mostrar la información registrada de forma organizada en consola.

---

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py        # Expone las clases del paquete (Producto, Cliente)
│   ├── producto.py        # Clase Producto (entidad del menú)
│   └── cliente.py         # Clase Cliente (persona registrada)
├── servicios/
│   ├── __init__.py        # Expone la clase del paquete (Restaurante)
│   └── restaurante.py     # Clase Restaurante (servicio que administra las listas)
└── main.py                # Punto de arranque del programa
README.md                  # Documentación del proyecto (raíz del repositorio)
```

### Responsabilidad de cada archivo

- **modelos/producto.py:** define la clase `Producto`, con atributos como nombre, categoría, precio, cantidad disponible y estado.
- **modelos/cliente.py:** define la clase `Cliente`, con atributos como nombre completo, cédula, edad, correo y tipo de cliente.
- **servicios/restaurante.py:** define la clase `Restaurante`, que gestiona las listas de productos y clientes mediante métodos propios.
- **main.py:** crea los objetos, los agrega al servicio principal y muestra la información en consola.

---

## Tipos de datos utilizados en las clases

| Clase | Atributo | Tipo de dato | Justificación |
|-------|----------|--------------|---------------|
| `Producto` | `nombre` | `str` | Texto del nombre del producto |
| `Producto` | `categoria` | `str` | Texto del tipo de producto |
| `Producto` | `precio` | `float` | Valor con decimales (precio) |
| `Producto` | `cantidad_disponible` | `int` | Número entero de unidades |
| `Producto` | `esta_disponible` | `bool` | Estado lógico (verdadero/falso) |
| `Cliente` | `nombre_completo` | `str` | Texto del nombre del cliente |
| `Cliente` | `cedula` | `str` | Identificación como texto (no se opera) |
| `Cliente` | `edad` | `int` | Número entero de años |
| `Cliente` | `correo_electronico` | `str` | Texto del correo de contacto |
| `Cliente` | `es_cliente_frecuente` | `bool` | Estado lógico del tipo de cliente |
| `Restaurante` | `nombre_restaurante` | `str` | Texto del nombre del restaurante |
| `Restaurante` | `lista_productos` | `list` | Lista de objetos `Producto` |
| `Restaurante` | `lista_clientes` | `list` | Lista de objetos `Cliente` |

---

## Convenciones de nombres aplicadas

- **PascalCase** para clases: `Producto`, `Cliente`, `Restaurante`.
- **snake_case** para variables, atributos, métodos y archivos: `cantidad_disponible`, `agregar_producto`, `producto.py`.

---

## Cómo ejecutar el programa

1. Ubicarse dentro de la carpeta `restaurante_app/`.
2. Ejecutar el archivo principal:

```bash
python main.py
```

El programa mostrará en consola el menú de productos, los clientes registrados y un resumen general del sistema.

---

## Reflexión

El uso de **identificadores descriptivos** hace que el código sea claro y fácil de entender: un nombre como `cantidad_disponible` comunica de inmediato su propósito, a diferencia de nombres genéricos como `x` o `dato`, lo que facilita el mantenimiento y reduce errores.

Elegir **tipos de datos adecuados** garantiza coherencia con la naturaleza de cada atributo: usar `float` para el precio, `int` para las cantidades y `bool` para los estados evita inconsistencias y refleja correctamente la información del mundo real.

Finalmente, las **listas** permiten almacenar y administrar varios objetos relacionados de forma ordenada dentro de un proyecto **modular**. Separar el código en carpetas (`modelos` y `servicios`) y comunicar los archivos mediante importaciones hace que el proyecto sea más organizado, escalable y reutilizable, aplicando así buenas prácticas de programación.
