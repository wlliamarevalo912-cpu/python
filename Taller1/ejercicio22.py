#Capture el peso y la altura de una persona,
#calcule el IMC y determine si dicha persona está en sobrepeso, peso normal o desnutrición.
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)

print(f"Su IMC es: {imc:.2f}")

if imc < 18.5:
    print("Está en desnutrición.")
elif 18.5 <= imc < 25:
    print("Tiene un peso normal.")
elif imc >= 25:
    print("Está en sobrepeso.")