README - Sistema de Gestión de Inventario

Descripción

Este programa permite gestionar un inventario de productos utilizando una base de datos SQLite. El sistema ofrece opciones para agregar, mostrar, actualizar, eliminar, buscar productos y generar un reporte de bajo stock.

Requisitos

Python 3.x

Biblioteca SQLite3 integrada en Python

Configuración

Asegúrate de tener Python 3 instalado.

Descarga el archivo inventario.py.

Ejecuta el programa con el siguiente comando:

python inventario.py

Funciones principales

1. Añadir nuevos productos

Permite ingresar productos al inventario solicitando datos como nombre, cantidad, precio, descripción y categoría.

2. Mostrar productos almacenados

Muestra una lista completa de los productos guardados en la base de datos.

3. Actualizar productos

Actualiza la información de un producto según su ID.

4. Eliminar productos

Elimina un producto del inventario según su ID.

5. Buscar producto

Busca un producto específico utilizando su ID y muestra sus detalles.

6. Reporte de bajo stock

Muestra productos cuyo stock es inferior a 25 unidades.

7. Salir

Finaliza el programa.

Estructura de la base de datos

Tabla Producto:

id: Identificador único, entero, autoincremental (clave primaria).

Nombre: Nombre del producto.

Cantidad: Cantidad disponible.

Precio: Precio del producto.

Descripcion: Descripción detallada.

Categoria: Categoría del producto.

Advertencias y Consideraciones

Asegúrate de realizar copias de seguridad de la base de datos.

No interrumpas el programa mientras esté realizando operaciones de escritura en la base de datos.

Créditos

Desarrollado por Salinas Dylan.