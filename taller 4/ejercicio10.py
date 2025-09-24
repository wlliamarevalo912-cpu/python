matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mostrar matriz
print("Matriz:")
for fila in matriz:
    print(fila)

# Diagonal principal: 1 + 5 + 9
diagonal = sum(matriz[i][i] for i in range(3))
print("Suma de la diagonal principal:", diagonal)

# Segunda columna: 2 + 5 + 8
segunda_col = sum(fila[1] for fila in matriz)
print("Suma de la segunda columna:", segunda_col)
