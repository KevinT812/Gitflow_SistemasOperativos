# generar_datos.py
import random

def generar_archivo(nombre, cantidad):
    with open(nombre, "w") as f:
        for _ in range(cantidad):
            f.write(f"{random.randint(1, 100000)}\n")

# Crear archivos
generar_archivo("datos/numeros_10000.txt", 10000)
generar_archivo("datos/numeros_30000.txt", 30000)

print("Archivos generados correctamente.")
