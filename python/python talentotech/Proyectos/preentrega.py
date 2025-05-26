
inventario = []
while True :

    print("\n Menu de Almacen")
    print("1: Añadir nuevos productos")
    print("2: Mostrar productos almacenados")
    print("3: Salir")


    opcion = int(input("Elige una opcion: "))

#agregar productos
    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        
        cantidad = int(input("Ingrese la cantidad del producto: "))

        producto = [nombre,cantidad]

        inventario.append(producto)
        print("carga exitosa")



#mostrar productos almacenados
    elif opcion == 2 :

        indice = 0
        
        while indice < len(inventario):
            print(f"{indice + 1}. Nombre:  {inventario[indice][0]}, Cantidad: {inventario[indice][1]}   ")

            indice += 1



    elif opcion == 3 :
         print("adios")
         break    
#salir
    else :
        print("opcion invalida, ingrese de nuevo una opcion")