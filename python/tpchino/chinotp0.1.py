tanquenafta = float(input("Cantidad de litros de nafta del auto: "))

kilometro_por_ruta = 14.1

kilometro_por_ciudad = 10.3

viaje_por_ruta = tanquenafta * kilometro_por_ruta

viaje_por_ciudad = tanquenafta * kilometro_por_ciudad

final_viaje_r = str(viaje_por_ruta)
final_viaje_c = str(viaje_por_ciudad)
print ("Por ruta viajas ", final_viaje_r +  " cantidad de kilometros")

print("por ciudad viaja ", final_viaje_c +  " cantidad de kilometros")



