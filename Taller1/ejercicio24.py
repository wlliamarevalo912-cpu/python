"""Una empresa decide otorgar un bono de temporada a sus empleados de la siguiente manera:
A empleados que sean estrato 1 les dará un 35% extra sobre su salario
A empleados que sean estrato 2 les dará un 30% extra sobre su salario 
A empleados que sean estrato 3 les dará un 25% extra sobre su salario
A empleados que sean estrato 4 les dará un 20% extra sobre su salario"""
# Capturar el salario del empleado
salario = float(input("Ingrese el salario del empleado: "))

# Capturar el estrato del empleado
estrato = int(input("Ingrese el estrato del empleado (1 a 4): "))

# Inicializar el bono en 0
bono = 0

# Determinar el porcentaje de bono según el estrato
if estrato == 1:
    bono = salario * 0.35
elif estrato == 2:
    bono = salario * 0.30
elif estrato == 3:
    bono = salario * 0.25
elif estrato == 4:
    bono = salario * 0.20
else:
    print("Estrato no válido. Debe estar entre 1 y 4.")

# Mostrar resultados si el estrato es válido
if 1 <= estrato <= 4:
    salario_total = salario + bono
    print(f"\nBono otorgado: ${bono:.2f}")
    print(f"Salario total con bono: ${salario_total:.2f}")