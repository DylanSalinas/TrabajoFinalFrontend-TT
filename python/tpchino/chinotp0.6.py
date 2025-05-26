notas_alumnos = 0

cantidad_de_alumnos = 0

while True :
    notas = float(input("nota de alumno: "))

    if notas == -1:
        break   

    notas_alumnos += notas

    cantidad_de_alumnos += 1

    promedio_curso = notas_alumnos // cantidad_de_alumnos


print("el promedio del curso es: ", promedio_curso)


