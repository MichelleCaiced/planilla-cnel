# Simulación de planilla de consumo eléctrico CNEL EP

# Entrada de datos
cliente = input("Ingrese el nombre del cliente: ")
suministro = input("Ingrese el número de suministro: ")
consumo_kwh = float(input("Ingrese la cantidad de energía consumida (kWh): "))

# Parámetros fijos
precio_unitario = 0.10
iva_porcentaje = 0.15

# Cálculos
subtotal = consumo_kwh * precio_unitario
iva = subtotal * iva_porcentaje
total = subtotal + iva

# Salida con formato
print("===============================================")
print("CNEL EP - UNIDAD DE NEGOCIO")
print("PLANILLA DE ENERGÍA ELÉCTRICA")
print("===============================================\n")

print("Planilla N.º: 000001")
print(f"Cliente:      {cliente.upper()}")
print(f"Suministro:   {suministro}")
print("-----------------------------------------------")
print("N.º  DESCRIPCIÓN         CONSUMO   V. UNITARIO   TOTAL")
print(f"1    Energía eléctrica   {consumo_kwh:.0f} kWh   USD {precio_unitario:.2f}     USD {subtotal:.2f}")
print("-----------------------------------------------")
print(f"SUBTOTAL:     USD {subtotal:.2f}")
print(f"IVA 15 %:     USD {iva:.2f}")
print(f"TOTAL:        USD {total:.2f}")
print("===============================================")
print("GRACIAS POR REALIZAR SU PAGO")
print("===============================================")
