import sqlite3

conexion = sqlite3.connect("inventario2.db")
# definir cursor
cursor = conexion.cursor()

#crear tabla 

cursor.execute("""
        CREATE TABLE IF NOT EXISTS Producto (
        Nombre TEXT NOT NULL,
        Cantidad INTEGER NOT NULL,
        Precio REAL NOT NULL,
        Descripcion TEXT,
        Categoria TEXT                                   
            )
""")
#Inserat info


#cursor.execute("INSERT INTO Producto (Codigo, Nombre, Cantidad, Precio) VALUES (1,'Manzana',10,100.5)")

#insertar multiple informacion

lista_producto = [
    ["Manzana", 10, 100.5],
    ["Pera", 10, 110.5],
    ["Naranja", 10, 90.5]
]
cursor.executemany("""
    INSERT INTO Producto (Codigo, Nombre, Cantidad, Precio, Descripcion, Categoria) VALUES (?,?,?)     
 """,lista_producto)

#eliminar producto

#cursor.execute("DELETE FROM Producto WHERE Nombre = 'Manzana'")

#Guardar cambios

conexion.commit()



#cerrar conexion

conexion.close()