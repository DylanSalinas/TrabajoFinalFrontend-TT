
import sqlite3

conexion = sqlite3.connect("inventario.db")
# definir cursor
cursor = conexion.cursor()

#crear tabla 

cursor.execute("""
        CREATE TABLE IF NOT EXISTS Producto (
        Codigo INTEGER NOT NULL,
        Nombre TEXT NOT NULL,
        Cantidad INTEGER NOT NULL,
        Precio REAL NOT NULL,
        Descripcion TEXT,
        Categoria TEXT                                   
            )
""")

#Guardar cambios
def guardar():
    conexion.commit()

#cerrar conexion
def cerrar_conexion():
    conexion.close()

#Funcion para agregar un producto
def agregar_productos():

    cod_serie = input("Ingresa el codigo serie del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese el stock del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    descripcion = input("ingrese la descripcion del producto: ")
    categoria = input("ingrese la categoria del producto: ")

    cursor.execute("""
    INSERT INTO Producto (Codigo, Nombre, Cantidad, Precio, Descripcion, Categoria) VALUES (?,?,?,?,?,?)     
    """, (cod_serie, nombre, cantidad, precio, descripcion, categoria))
    print("Carga exitosa")

#Funcion mostrar inventario
def mostrar_inventario():
    cursor.execute("SELECT * FROM Producto")
    productos = cursor.fetchall()

    if not productos:
        print("El inventario esta vacio.")
    else:
        print(" Productos en el inventario:")

    for producto in productos:            

        print(f"Codigo {producto[0]}")
        print(f"    Nombre: {producto[1]}")
        print(f"    Cantidad: {producto[2]}")
        print(f"    precio: {producto[3]}")
        print(f"    descripcion: {producto[4]}")
        print(f"    Categoria: {producto[5]}")

#Funcion Actualizar productos
def actualizar_productos():
    codigo_producto = input("Ingrese el codigo del producto que desea actualizar: ")

    cursor.execute("SELECT * FROM Producto WHERE CODIGO = ?", (codigo_producto))
    producto = cursor.fetchone()
    if not codigo_producto:
        print("Producto no encontrado.")

    else:
        #datos del producto almacenado
        print(f"Codigo {producto[0]}")
        print(f"    Producto: {producto[1]}")
        print(f"    Cantidad actual: {producto[2]}")
        print(f"    Precio actual: {producto[3]}")
        print(f"    Descripcion actual: {producto[4]}")
        print(f"    Categoria actual: {producto[5]}")  

        #datos para actualizar el producto
        nombre = input("Nuevo nombre (deje en blanco para no cambiar): ") or producto[1]
        cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ") or producto[2]
        precio = input("Nuevo precio (deje en blanco para no cambiar): ") or producto[3]
        descripcion = input("Nueva descripción (deje en blanco para no cambiar): ") or producto[4]
        categoria = input("Nueva categoría (deje en blanco para no cambiar): ") or producto[5] 

        cursor.execute("""
        UPDATE Producto
        SET Nombre = ?, Cantidad = ?, Precio = ?, Descripcion = ?, Categoria = ?
        WHERE Codigo = ?
        """, (nombre, cantidad, precio, descripcion, categoria, codigo_producto))

#Funcion para borrar un producto
def eliminar_producto():
    codigo = input("Ingrese el codigo del producto que desea eliminar: ")
    

    cursor.execute("DELETE FROM Producto WHERE Codigo = ?", codigo)

    print("Producto eliminado correctamente")




#Funcion buscar producto
def buscar_producto():
    codigo_producto = input("Ingrese el codigo del producto que desea buscar: ")

    cursor.execute("SELECT * FROM Producto WHERE CODIGO = ?", (codigo_producto))
    producto = cursor.fetchone()
    if not codigo_producto:
        print("Producto no encontrado.")

    else:
        #datos del producto almacenado
        print(f"Codigo {producto[0]}")
        print(f"    Producto: {producto[1]}")
        print(f"    Cantidad actual: {producto[2]}")
        print(f"    Precio actual: {producto[3]}")
        print(f"    Descripcion actual: {producto[4]}")
        print(f"    Categoria actual: {producto[5]}")


#Funcion reporte bajo stock
def reporte_bajo_stock():
    cursor.execute("SELECT * FROM Producto")
    productos = cursor.fetchall()
    if not productos:
        print("El inventario esta vacio.")
    for productos in productos:
        if productos[2] < 25:
            print(f"Producto con bajo stock: {productos[1]} - Cantidad: {productos[2]}")





def menu_principal():
    while True :

        print("\n Menu de Almacen")
        print("1: Añadir nuevos productos")
        print("2: Mostrar productos almacenados")
        print("3: Actualizar productos")
        print("4: Eliminar productos")
        print("5: Buscar producto")
        print("6: Reporte de bajo stock")
        print("7: Salir")
        opcion = int(input("Elige una opcion: "))

 # Opciones del menú
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





#mostrar mayor stock
#mostrar inventario ordenado segun stock
#registrar transaccion