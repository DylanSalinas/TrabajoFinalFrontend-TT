

# inventario = {}


# for i in range(3):
#     producto = input("Ingrese el nombre del producto: ")
#     precio = float(input("Ingrese el precio del producto: "))
#     inventario[producto] = precio
     
#     break

# for clave, valor in inventario.items():
#     print(f"Elproducto {clave} vale ${valor}")







productos = {
    "manzanas": 50,
    "naranjas": 30,
    "peras": 25,
}


while True:

    producto = input("Ingrese el producto que desea buscar o 'salir' si desea finalizar: ").lower()
    
    if producto == "salir":
        print("adios")
        break

    else:
        value = productos.get(producto, "producto no encontrado")


        if value == "producto no encontrado":
            print("producto no encontrado")

        else:
            print(f"{producto()} : {value}")