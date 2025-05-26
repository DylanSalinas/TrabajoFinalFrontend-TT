import sqlite3 
# Conexión a la base de datos SQLite
conexion = sqlite3.connect("inventario.db")

# Definir el cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Crear la tabla Producto si no existe
cursor.execute("""
        CREATE TABLE IF NOT EXISTS Producto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        Nombre TEXT NOT NULL,                  
        Cantidad INTEGER NOT NULL,            
        Precio REAL NOT NULL,                 
        Descripcion TEXT,                     
        Categoria TEXT                        
            )
""")

# Guardar cambios en la base de datos
def guardar():
    conexion.commit()

# Cerrar la conexión con la base de datos
def cerrar_conexion():
    conexion.close()

# Agregar un nuevo producto al inventario
def agregar_productos():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese el stock del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    descripcion = input("Ingrese la descripción del producto: ")
    categoria = input("Ingrese la categoría del producto: ")

    # Insertar datos en la tabla Producto
    cursor.execute("""
    INSERT INTO Producto (Nombre, Cantidad, Precio, Descripcion, Categoria) VALUES (?,?,?,?,?)    
    """, (nombre, cantidad, precio, descripcion, categoria))
    print("Carga exitosa")

# Mostrar el inventario completo
def mostrar_inventario():
    cursor.execute("SELECT * FROM Producto")
    productos = cursor.fetchall()  # Recuperar todos los productos

    if not productos:
        print("El inventario está vacío.")
    else:
        print("Productos en el inventario:")

    for producto in productos:            
        print(f"Código {producto[0]}")
        print(f"    Nombre: {producto[1]}")
        print(f"    Cantidad: {producto[2]}")
        print(f"    Precio: {producto[3]}")
        print(f"    Descripción: {producto[4]}")
        print(f"    Categoría: {producto[5]}")

# Actualizar datos de un producto existente
def actualizar_productos():
    id_producto = input("Ingrese el código del producto que desea actualizar: ")
    cursor.execute("SELECT * FROM Producto WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()

    if not producto:
        print("Producto no encontrado.")
    else:
        print(f"Código {producto[0]} - Producto actual: {producto[1]}")

        # Solicitar nuevos datos (con valores predeterminados)
        nombre = input("Nuevo nombre (deje en blanco para no cambiar): ") or producto[1]
        cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ") or producto[2]
        precio = input("Nuevo precio (deje en blanco para no cambiar): ") or producto[3]
        descripcion = input("Nueva descripción (deje en blanco para no cambiar): ") or producto[4]
        categoria = input("Nueva categoría (deje en blanco para no cambiar): ") or producto[5]

        # Actualizar datos en la base de datos
        cursor.execute("""
        UPDATE Producto
        SET Nombre = ?, Cantidad = ?, Precio = ?, Descripcion = ?, Categoria = ?
        WHERE id = ?
        """, (nombre, cantidad, precio, descripcion, categoria, id_producto))

# Eliminar un producto por su ID
def eliminar_producto():
    id_producto = input("Ingrese el código del producto que desea eliminar: ")
    cursor.execute("DELETE FROM Producto WHERE id = ?", (id_producto,))
    print("Producto eliminado correctamente")

# Buscar un producto por su ID
def buscar_producto():
    id_producto = input("Ingrese el código del producto que desea buscar: ")
    cursor.execute("SELECT * FROM Producto WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()

    if not producto:
        print("Producto no encontrado.")
    else:
        print(f"Código {producto[0]}")
        print(f"    Producto: {producto[1]}")
        print(f"    Cantidad: {producto[2]}")
        print(f"    Precio: {producto[3]}")
        print(f"    Descripción: {producto[4]}")
        print(f"    Categoría: {producto[5]}")

# Generar reporte de productos con bajo stock
def reporte_bajo_stock():
    cursor.execute("SELECT * FROM Producto")
    productos = cursor.fetchall()

    if not productos:
        print("El inventario está vacío.")

    for producto in productos:
        if producto[2] < 25:  # Verifica si el stock es menor a 25
            print(f"Producto con bajo stock: {producto[1]} - Cantidad: {producto[2]}")

# Menú principal del sistema
def menu_principal():
    while True:
        print("\nMenú de Almacén")
        print("1: Añadir nuevos productos")
        print("2: Mostrar productos almacenados")
        print("3: Actualizar productos")
        print("4: Eliminar productos")
        print("5: Buscar producto")
        print("6: Reporte de bajo stock")
        print("7: Salir")

        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            agregar_productos()
        elif opcion == 2:
            mostrar_inventario()
        elif opcion == 3:
            actualizar_productos()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            buscar_producto()
        elif opcion == 6:
            reporte_bajo_stock()
        elif opcion == 7:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 7.")

menu_principal()
guardar()
cerrar_conexion()