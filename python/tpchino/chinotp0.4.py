
limite_tarjeta = int(input("limite de tarjeta: "))




if  limite_tarjeta <= 250000 : 
    porcentual = 0.25

elif limite_tarjeta <= 500000:
    porcentual = 0.35

elif limite_tarjeta <= 750000:
    porcentual = 0.40

elif limite_tarjeta > 750000:
    porcentual = 0.50


aumento = str(limite_tarjeta * porcentual)

print("aumento de limite: ", aumento)
