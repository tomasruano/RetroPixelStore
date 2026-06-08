# RetroPixel Store

Sistema de gestión de alquiler y venta de productos de entretenimiento desarrollado en Python.

---

## Objetivo

El propósito del programa es centralizar la administración de películas y videojuegos, permitiendo registrar, modificar, eliminar y visualizar productos para facilitar el control del inventario de la tienda.

---

## Funcionalidades

Las principales funcionalidades implementadas son:

* Alta de productos.
* Baja de productos.
* Modificación de productos.
* Visualización general del catálogo.
* Generación automática de productos para pruebas.
* Ordenamiento de productos según stock disponible y en caso de igualdad según orden alfabético.

---

## Requisitos

Para ejecutar el proyecto se requiere:

* Python 3.x

---

## Instalación

1. Descargar o clonar el proyecto.
2. Abrir una terminal.
3. Ubicarse en la carpeta del proyecto.

---

## Ejecución

Ejecutar el siguiente comando:

bash
python mainTPO.py

---

## Estructura del Proyecto

```text
RetroPixelStore/
│
├── mainTPO.py
├── FuncionesTPO.py
├── DatosTPO.py
├── MenusTPO.py
└── README.md
```

---

## Organización del Código

### mainTPO.py

Contiene el programa principal y controla el flujo general de ejecución mediante el menú interactivo.

### FuncionesTPO.py

Contiene las funciones encargadas de realizar las operaciones principales del sistema:

* Registrar productos.
* Eliminar productos.
* Modificar productos.
* Generar el informe general.
* Buscar elementos dentro de las listas.

### DatosTPO.py

Contiene:

* Las listas paralelas donde se almacenan los productos registrados.
* Las opciones válidas para cada atributo.
* Los datos utilizados para la generación aleatoria de productos.

### MenusTPO.py

Contiene las funciones encargadas de mostrar los distintos menús utilizados por el sistema.

---

## Tecnologías Utilizadas (hasta ahora)

* Python
* random

---

## Conceptos de Programación Aplicados

Durante el desarrollo se utilizaron los siguientes conceptos:

* Variables
* Entrada y salida de datos
* Estructuras condicionales
* Ciclos repetitivos
* Funciones
* Listas
* Matrices
* Modularización
* Validación de datos
* Ordenamiento de datos
* Búsqueda secuencial

---

## Integrantes del Equipo

* Tomas Ruano
* Gaspar Divano
* Ignacio Diaz
* Tomas Sobrino
* Agustin Fani
---

## Distribución de Tareas

Todos los integrantes contribuimos en cada función pero se asignaron los siguientes responsables principales para cada bloque funcional:
* Agustín Fani: Eliminar producto
* Tomas Ruano: Registrar producto 
* Tomas Sobrino: Modificar producto
* Ignacio Díaz: Buscar índice, main y menús 
* Gaspar Divano: Informe general
---

## Decisiones de Diseño

-Se separó el código en cuatro módulos según su responsabilidad: datos, funciones, menús y programa principal.
-Se validaron todas las entradas del usuario con ciclos while, usando listas de opciones predefinidas para evitar datos inválidos.
-Se implementó una función auxiliar buscar_indice reutilizable debido a que no se podía usar la función index().
-Para el informe general, las listas se convierten en una matriz temporal para aplicar el ordenamiento burbuja sin modificar los datos originales.

---
## Repositorio GitHub

https://github.com/tomasruano/RetroPixelStore

---

## Licencia

Proyecto académico desarrollado para una asignatura de programación (Pensamiento Computacional, Algoritmia y Programación).

Su finalidad es exclusivamente educativa.
