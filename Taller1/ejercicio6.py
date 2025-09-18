#cree un programa que pida un angulo y regrese el seno,
# el coseno y la tangente  del mismo. pista: use la clase "math".
import math
angulo_grados = float(input("ingrese un angulo en grados: "))
angulo = 10
angulo_radiante = math.radians(angulo_grados)

seno = math.sin(angulo_radiante)
coseno = math.cos(angulo_grados)
tangente = math.tan(angulo_radiante)

print(f"\nAngulo en grados: {angulo_grados}°")
print(f"seno: {seno: .4f}")
print(f"coseno: {coseno: .4f}")
print(f"tangente: {tangente: 4f}")

