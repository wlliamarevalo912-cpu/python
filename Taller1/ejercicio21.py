#Capture el salario de una persona y determine si dicho salario es integral.
salario = float(input("Ingrese su salario mensual: "))
salario_minimo = 1300000  # Puedes cambiar esto según la normativa de tu país

if salario >= 13 * salario_minimo:
    print("Tiene un salario integral.")
else:
    print("No tiene un salario integral.")