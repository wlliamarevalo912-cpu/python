#capturar dos numeros que sean mayor, menor e iguales

num1 = float(input("ingrese el primer numero:  "))
num2 = float(input("ingrese el primer numero:  "))

if num1 > num2:
    print(f"el numero mayor es:{num1}")
    print(f"el numero menor es:{num2}")

elif num2 > num1:
    print(f"el numero mayor es: {num2}")
    print(f"el numero menor es: {num1}")

else:
    print("ambos numeros son iguales")

