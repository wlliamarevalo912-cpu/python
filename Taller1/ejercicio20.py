#capture el sexo de una persona y salude a dicha de persona manera adecuada segun su sexo
sexo = input("Ingrese su sexo (M para masculino, F para femenino): ").strip().upper()

if sexo == 'M':
    print("¡Hola señor!")
elif sexo == 'F':
    print("¡Hola señora!")
else:
    print("Sexo no reconocido.")