# RetroPixel Store

Sistema de gestión de productos de entretenimiento desarrollado en Python.

---

## Objetivo

El propósito del programa es centralizar la administración de películas y videojuegos, permitiendo registrar, modificar, eliminar y visualizar productos para facilitar el control del inventario de la tienda.

---

## Funcionalidades

Las principales funcionalidades implementadas son:

* Alta de productos mediante carga manual o aleatoria.
* Baja de productos con validación de eliminación.
* Modificación de productos existentes.
* Visualización general del catálogo.

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

```bash
python mainTPO.py
```

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

Contiene el programa principal y controla el flujo general de ejecución mediante un menú interactivo.

Funciones principales:

* Inicialización de los datos del sistema.
* Ejecución del menú principal.
* Control de las operaciones de alta, baja, modificación e informe.

---

### FuncionesTPO.py

Contiene la lógica principal del sistema.

Incluye funciones para:

#### Registro de productos

* Registro manual de productos.
* Registro aleatorio de productos.
* Generación de datos aleatorios.
* Validación de títulos duplicados.

#### Eliminación de productos

* Verificación de productos eliminables.
* Confirmación de eliminación.
* Eliminación segura de registros.

#### Modificación de productos

* Búsqueda de productos por título.
* Selección de atributos a modificar.
* Actualización de información.

#### Informe General

* Conversión de listas paralelas en una matriz.
* Ordenamiento burbuja por stock.
* Visualización tabulada de productos.

#### Funciones auxiliares

* Búsqueda secuencial.
* Validación de enteros.
* Validación de números reales.
* Validación de opciones.
* Verificación de existencia en listas.
* Almacenamiento de nuevos productos.

---

### DatosTPO.py

Contiene:

* Los productos precargados en el sistema.
* Las listas paralelas utilizadas para almacenar la información.
* Las opciones válidas para cada atributo.
* Los datos utilizados para la generación aleatoria de productos.

---

### MenusTPO.py

Contiene las funciones encargadas de mostrar los distintos menús utilizados por el sistema.

Incluye:

* Menú principal.
* Menú de modificación de atributos.

---

## Tecnologías Utilizadas

* Python
* random

---

## Conceptos de Programación Aplicados

Durante el desarrollo se utilizaron los siguientes conceptos:

* Variables
* Funciones
* Modularización
* Parámetros
* Retorno de valores
* Listas
* Listas paralelas
* Matrices
* Estructuras condicionales
* Ciclos repetitivos
* Validación de datos
* Búsqueda secuencial
* Ordenamiento burbuja
* Generación aleatoria de datos
* Manipulación de listas mediante append() y pop()

---

## Integrantes del Equipo

* Tomas Ruano
* Gaspar Divano
* Ignacio Diaz
* Tomas Sobrino
* Agustin Fani

---

## Distribución de Tareas

### Tomas Ruano

* Registro manual de productos.
* Registro aleatorio de productos.
* Funciones de búsqueda y validación.
* Control de títulos duplicados.

### Gaspar Divano

* Creación de datos iniciales.
* Generación del informe general.
* Conversión de listas paralelas a matriz.
* Ordenamiento burbuja.

### Ignacio Diaz

* Menú principal.
* Flujo principal del programa.
* Validación de números reales.
* Funciones auxiliares para carga de productos.

### Tomas Sobrino

* Modificación de productos.
* Aplicación de cambios en atributos.
* Validación de opciones.
* Almacenamiento de productos.

### Agustin Fani

* Eliminación de productos.
* Verificación de productos eliminables.
* Eliminación por índice.
* Obtención de datos para generación aleatoria.

---

## Decisiones de Diseño

* Se separó el proyecto en módulos independientes para mejorar la organización y mantenimiento del código.
* Se utilizaron listas paralelas para almacenar la información de los productos.
* Se implementó una función propia de búsqueda debido a la restricción de no utilizar index().
* Se validaron todas las entradas del usuario mediante estructuras repetitivas.
* Se impidió el registro de productos con títulos duplicados.
* Se creó una matriz temporal para generar el informe sin modificar las listas originales.
* Se implementó un ordenamiento burbuja para mostrar los productos según su stock disponible.

---

## Licencia

Proyecto académico desarrollado para la asignatura Pensamiento Computacional, Algoritmia y Programación.

Su finalidad es exclusivamente educativa.