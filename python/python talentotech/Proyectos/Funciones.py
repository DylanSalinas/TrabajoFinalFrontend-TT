

inventario = {}

opcion = 0

#agregar productos

def añadir_productos():

        cod_serie = input("Ingresa el codigo serie del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese el stock del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        descripcion = input("ingrese la descripcion del producto: ")
        categoria = input("ingrese la categoria del producto: ")

        producto = {
              "Nombre": nombre,
              "Cantidad": cantidad,
              "Precio": precio,
              "Descripcion": descripcion,
              "Categoria": categoria

        }

        inventario[cod_serie] = producto
añadir_productos()
añadir_productos()
#mostrar productos almacenados
#  
def mostrar_inventario():
        for clave, valor in inventario.items():
                print(f"Codigo {clave}")
                print(f"    Nombre: {valor['Nombre']}")
                print(f"    Cantidad: {valor['Cantidad']}")
                print(f"    precio: {valor['Precio']}")
                print(f"    descripcion: {valor['Descripcion']}")
                print(f"    Categoria: {valor['Categoria']}")
mostrar_inventario()



#Actualizar productos

#def actualizar_producto():





#Eliminar producto

#def eliminar_producto():


#Buscar Producto

#def buscar_producto():


#Reporte de bajo stock

#def reporte_bajo_stock():



#funcion de menu principal

# def menu_principal():
#        while True :

#                print("\n Menu de Almacen")
#                print("1: Añadir nuevos productos")
#                print("2: Mostrar productos almacenados")
#                print("3: Actualizar productos")
#                print("4: Eliminar productos")
#                print("5: Buscar producto")
#                print("6: Reporte de bajo stock")
#                print(": Salir")