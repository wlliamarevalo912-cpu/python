numeros = [1,2,2,3,4,4,4,5,6,6,6,6]
conteo = {}

for num in set(numeros):  # Usamos set para no repetir
    conteo[num] = numeros.count(num)

print("Conteo de números:")
for k, v in conteo.items():
    print(f"{k} aparece {v} veces")
