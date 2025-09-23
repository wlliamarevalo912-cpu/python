"""2.Escribe un programa que pida un número entero positivo n y
 calcule la suma de todos los números pares entre 1 y n."""


n = int(input("Ingrese un número entero positivo: "))
suma_pares = 0

for i in range(2, n + 1, 2):  # Va de 2 en 2
    suma_pares += i

print(f"La suma de todos los números pares entre 1 y {n} es: {suma_pares}")