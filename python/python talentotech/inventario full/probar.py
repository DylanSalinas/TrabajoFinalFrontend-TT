import sqlite3

conexion = sqlite3.connect("probar.db")
# definir cursor
cursor = conexion.cursor()

#crear tabla 

cursor.execute("""
        CREATE TABLE IF NOT EXISTS Producto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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




def agregar_productos():

    cod_serie = input("Ingresa el codigo serie del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese el stock del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    descripcion = input("ingrese la descripcion del producto: ")
    categoria = input("ingrese la categoria del producto: ")

    cursor.execute("""
    INSERT INTO Producto (id, Nombre, Cantidad, Precio, Descripcion, Categoria) VALUES (?,?,?,?,?,?)     
    """, (cod_serie, nombre, cantidad, precio, descripcion, categoria))

agregar_productos()

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




def reporte_bajo_stock():
    cursor.execute("SELECT * FROM Producto")
    productos = cursor.fetchall()
    if not productos:
        print("El inventario esta vacio.")
    for Cantidad in productos:
        if Cantidad << 25:
            print("Bajo stock ")

mostrar_inventario()
guardar()
cerrar_conexion()