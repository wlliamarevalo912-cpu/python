agenda = {
    "Luis": "3110001111",
    "Ana": "3101234567",
    "Carlos": "3129876543"
}

print("Teléfono de Ana:", agenda["Ana"])  # Buscar

agenda["Luis"] = "3000000000"  # Cambiar número
del agenda["Carlos"]           # Eliminar contacto

print("Agenda actualizada:", agenda)
