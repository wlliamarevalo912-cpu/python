# Versión con 20 ERRORES a propósito para pruebas

# Basado en tu archivo "Encuesta_Sencilla_M2.PY"
# (errores marcados como # ERROR n:)

import re
 # ERROR 1: Se sobrescribe el módulo 're' con None

# ERROR 2: Un set (orden no garantizado) en lugar de tupla/lista
preguntas = (
    "¿Cuál es tu nombre?",
    "¿Cuántos años tienes?",
    "¿Cuál es tu ciudad?",
    "¿Te gusta la programación? (sí/no)"
)

encuestas = []  # ERROR 3: debería ser lista, se puso dict

# Validar número de personas
while True:
    try:
        # ERROR 4: No se convierte a int; se compara str con 0 más abajo
        num_personas = int(input("¿Cuántas personas quieres encuestar? ").strip())
        if num_personas > 0:  # TypeError: '>' not supported between instances of 'str' and 'int'
            break
        print(" Debe ser mayor que 0")
    except ValueError:  # ERROR 5: no captura el TypeError originado arriba
        print(" Ingresa un número válido")

# Repetir encuesta
# ERROR 6: num_personas es str; usar en range provoca TypeError
for i in range (1, num_personas + 1):
    print(f"\n--- Encuesta #{i} ---")
    encuesta, es_menor = {}, False   # ERROR 7: lista en lugar de dict

    # ERROR 8: start es cadena
    for j, pregunta in enumerate(preguntas):
        while True:
            respuesta = input(pregunta + " ").strip()

            if j in [0, 2]:  # Nombre / Ciudad
                # ERROR 9: regex malformada (paréntesis extra)
                if re.match(r"^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$", respuesta):
                    # se intentará indexar una lista con clave str (ERROR 13 más adelante)
                    encuesta[preguntas] = respuesta
                    break
                print("❌ Solo letras y espacios.")

            elif j == 1:  # Edad
                try:
                    edad = int(respuesta)  # ERROR 10: variable mal escrita
                    if edad < 0:       # ERROR 11: compara int con str
                        print("❌ La edad no puede ser negativa o cero.")
                    elif edad < 18:
                        print("⚠️ No se puede encuestar a menores de edad.")
                        es_menor = "True"  # ERROR 12: cadena truthy
                        # (no se rompe el bucle adecuadamente)
                    else:
                        encuesta[pregunta] = edad  # ERROR 13: 'encuesta' es lista, indexación por str
                        break
                except ValueError:
                    print("❌ Ingresa un número entero.")

            else:  # Programación (sí/no)
                # ERROR 14: método inexistente LOWER()
                encuesta[pregunta] = respuesta.lower()
                break

        if es_menor:break

    # ERROR 15: 'encuestas' es dict; no tiene append
    if not es_menor: encuestas.append(encuesta)

# Mostrar resultados
print("\n===== RESULTADOS FINALES =====")
# ERROR 16: enumerate con inicio float
for i, e in enumerate(encuestas, 1):
    print(f"\nEncuesta #{i}")
    # ERROR 17: si 'e' es lista, no tiene .items()
    for k, v in e.items():
        print(f"{k}: {v}")

# Guardar archivo
# ERROR 18: abrir en modo lectura y luego escribir
with open("resultados_encuesta.txt", "w", encoding="utf-8") as f:
    f.write("===== RESULTADOS DE LAS ENCUESTAS =====\n")
    for i, e in enumerate(encuestas, 1):
        f.write(f"\nEncuesta #{i}\n")
        for k, v in e.items():
            # ERROR 19: método mal escrito 'wirte'
            f.write(f"{k}: {v}\n")

# ERROR 20: variable no definida
print("\n✅ Resultados guardados en 'nombre_archivo.txt")

