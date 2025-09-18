#Capture tres números y determine cuál de ellos es el mayor, cual el menor y cuál es el del medio.
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

numeros = [n1, n2, n3]
numeros_ordenados = sorted(numeros)

print(f"El menor número es: {numeros_ordenados[0]}")
print(f"El número del medio es: {numeros_ordenados[1]}")
print(f"El mayor número es: {numeros_ordenados[2]}")