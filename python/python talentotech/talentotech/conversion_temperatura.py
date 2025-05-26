Celcius_kelvin = 273 #Valor utilizado para kconvertir de kelvin a celsius
#variable para conversion de fahrenheit a celcius

temperatura_c = float(input("Ingrese el valor de temperatura en C° "))

Celcius_fahrenheit =  temperatura_c * 1.8 + 32

temperatura_k = temperatura_c + Celcius_kelvin

#conversion f a c 1.8 * c + 32

#temperatura_F = temperatura_c + Celcius_fahrenheit


print("El valir en la temperatura expresada en C° es: ", temperatura_c)
print("El valor en la temperatura expresada en K° es: ", temperatura_k)
print("El valor de la temperatura expresada en Fahrenheit es: ",Celcius_fahrenheit)