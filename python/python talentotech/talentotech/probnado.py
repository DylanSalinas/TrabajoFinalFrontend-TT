costo_servicio = float(input("costo de servicio: "))

# calcular impuestos 
#iva 21%
costo_servicio_iva = costo_servicio * 0.21 
# pais 8%
costo_servicio_pais = costo_servicio * 0.08
#ganancias 30%
Costo_servicio_ganacia = costo_servicio * 0.30
# IIBB CABA 2%
costo_servicio_iibb = costo_servicio * 0.02

valor_final = costo_servicio + costo_servicio_iva + costo_servicio_pais + Costo_servicio_ganacia + costo_servicio_iibb
print("El Valor final a pagar es: ", valor_final) 