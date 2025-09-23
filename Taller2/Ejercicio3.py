"""3.Escribe un programa que presente un menú con opciones 
para realizar una operación matemática (suma, resta, multiplicación o división) 
entre dos números.El programa debe repetirse hasta que el usuario elija salir."""



while True:
    # Mostrar menú
    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    # Pedir opción
    opcion = input("Elige una operación (1-5): ")
    
    # Salir del programa
    if opcion == "5":
        print("¡Programa finalizado!")
        break
    
    # Validar opción
    if opcion not in ["1", "2", "3", "4"]:
        print("Opción inválida. Inténtalo de nuevo.")
        continue
    
    # Pedir números
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Error: Debes introducir números válidos.")
        continue
    
    # Realizar operación
    if opcion == "1":
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif opcion == "2":
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif opcion == "3":
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif opcion == "4":
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")