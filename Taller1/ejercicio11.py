#solicite el ingreso de una palabra y una letra,
#luego diga en que posicion esta la letra que usted indico.
palabra = input("ingrese la palabra: ")
letra = input("ingrese la letra: ")
posicion = palabra.find(letra) +1 # se pone +1 por que python cuenta desde cero
print(f"la posicion de las letras  son {posicion}")
