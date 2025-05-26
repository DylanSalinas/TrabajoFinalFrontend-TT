# numeros = [1,2,3,4,5]

# frutas = ["manzana", "pera", "durazno"]

# for numero in numeros:
#     print(frutas)




sumatoria_notas = 0

for i in range(3):
    nota = float(input("Ingresa la nota del examen: "))
    sumatoria_notas = nota + sumatoria_notas


    print("la nota se ingreso correctamente")


print(i)

print(f"Elpromedio es :{ sumatoria_notas / (i+1)}")