#capture dos numeros y determine cual de ellos es el mayor, cual el menor o sin son iguales.
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))

if num1 > num2:
    print(f"el mayor es: {num1}")
    print(f"el menor es: {num2}")
elif num2 > num1:
    print(f"el mayor es: {num2}")
    print(f"el menor es: {num1}")
else:
    print("ambos numeros son iguales")
