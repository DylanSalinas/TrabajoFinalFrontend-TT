precio_compra = float(input("Precio compra: "))

abona_con = float(input("cliente abona: "))

falta_guita = str(abona_con - precio_compra)

vuelto = str(precio_compra - abona_con)

if precio_compra <= abona_con :
   
   print("vuelto: ", vuelto)

elif precio_compra >= abona_con:
    print("falta: ", falta_guita )
