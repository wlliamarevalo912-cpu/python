#Tabla de multiplicar
numero = int(input("Ingrese un número entero: "))
print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    