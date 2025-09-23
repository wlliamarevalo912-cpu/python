"""4.Escribe un programa que pida un año y determine si es un año bisiesto o no. 
(Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400)."""
año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")