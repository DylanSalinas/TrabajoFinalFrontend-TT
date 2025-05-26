asientos_conferencia = float(input("cantidad de asientos: "))

invitados_conferencia = float(input("cantidad de invitados: "))

necesitamos_sillas = str(invitados_conferencia - asientos_conferencia)

if asientos_conferencia >= invitados_conferencia :
    print("todos sentados :D")
elif asientos_conferencia < invitados_conferencia :
    print("Faltan: ", necesitamos_sillas + "sillas")