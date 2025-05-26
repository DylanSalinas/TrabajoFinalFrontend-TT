
total = 0

cantidad_de_productos = 0

while True:
    precio = float(input("precio de producto: "))

    if precio == 0 :
        break
    
    total += precio


    cantidad_de_productos += 1

print("total a pagar: $ ", total)
print("cantidad de productos: ", cantidad_de_productos)