import time
import csv
import matplotlib.pyplot as plt
from algoritmos.quicksort import quicksort
from algoritmos.hashing_simple import hashing_simple

def leer_datos(ruta_archivo):
    """
    Lee los datos numéricos desde un archivo de texto.

    Cada línea del archivo debe contener un número entero. Los datos
    se convierten a una lista de enteros para su posterior análisis.

    Parámetros:
        ruta_archivo (str): Ruta del archivo .txt que contiene los números.

    Retorna:
        list: Lista con los números leídos desde el archivo.
    """
    with open(ruta_archivo, "r") as f:
        return [int(line.strip()) for line in f]

def medir_tiempo(funcion, *args):
    """
    Mide el tiempo de ejecución de una función.

    Utiliza el reloj de alta precisión de Python (perf_counter)
    para registrar el tiempo que tarda en ejecutarse una función
    con los parámetros indicados.

    Parámetros:
        funcion (callable): Función que se desea medir.
        *args: Argumentos posicionales que se pasarán a la función.

    Retorna:
        float: Tiempo de ejecución en segundos.
    """
    inicio = time.perf_counter()
    funcion(*args)
    fin = time.perf_counter()
    return fin - inicio

def graficar_resultados(resultados, ruta_guardado):
    """
    Genera una gráfica comparativa entre QuickSort y Hashing Simple.

    Parámetros:
        resultados (list): Lista de tuplas con formato
            [(tamano, tiempo_quick, tiempo_hash), ...]
        ruta_guardado (str): Ruta donde se guardará la imagen.
    """
    tamanos = [r[0] for r in resultados]
    tiempos_quick = [r[1] for r in resultados]
    tiempos_hash = [r[2] for r in resultados]

    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, tiempos_quick, marker='o', label='QuickSort', linewidth=2)
    plt.plot(tamanos, tiempos_hash, marker='s', label='Hashing Simple', linewidth=2)
    plt.title("Comparación de tiempos de ejecución")
    plt.xlabel("Tamaño del dataset (números)")
    plt.ylabel("Tiempo (segundos)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(ruta_guardado)
    plt.show()

def main():
    """
    Ejecuta pruebas empíricas de rendimiento para QuickSort y Hashing Simple
    usando distintos archivos de datos.

    Para cada archivo de datos especificado, se mide el tiempo de ejecución
    de los algoritmos y se muestran los resultados en consola.
    """
    # Archivos de entrada a evaluar
    archivos = [
        ("datos/numeros_10000.txt", 10000),
        ("datos/numeros_30000.txt", 30000),
        ("datos/numeros_100000.txt", 100000),
        ("datos/numeros_300000.txt", 300000)
    ]

    print("\n=== VERIFICACIÓN EMPÍRICA DE QUICKSORT Y HASHING SIMPLE ===")

    resultados_quick = []
    resultados_hash = []

    print("\n=== FASE 1: Evaluación con QuickSort ===")
    for ruta, n in archivos:
        try:
            datos = leer_datos(ruta)
        except FileNotFoundError:
            print(f"\n[ERROR] No se encontró el archivo: {ruta}")
            continue

        t_quick = medir_tiempo(quicksort, datos.copy())
        resultados_quick.append((n, t_quick))
        print(f"Tamaño: {n} | Tiempo QuickSort: {t_quick:.6f} s")

    print("\n=== FASE 2: Evaluación con Hashing Simple ===")
    for ruta, n in archivos:
        try:
            datos = leer_datos(ruta)
        except FileNotFoundError:
            print(f"\n[ERROR] No se encontró el archivo: {ruta}")
            continue

        t_hash = medir_tiempo(hashing_simple, datos.copy(), n * 2)
        resultados_hash.append((n, t_hash))
        print(f"{n} | Tiempo Hashing Simple: {t_hash:.6f} s")

    # --- Aqui se unen los resultados en una sola lista para el CSV y la gráfica ---
    resultados = []
    for i in range(len(resultados_quick)):
        n = resultados_quick[i][0]
        t_quick = resultados_quick[i][1]
        t_hash = resultados_hash[i][1]
        resultados.append((n, t_quick, t_hash))

    ruta_csv = "evidencias/resultados_tiempos.csv"
    with open(ruta_csv,"w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Tamaño", "QuickSort (s)", "Hashing Simple (s)"])
        writer.writerows(resultados)
    print("-Resultados guardados en: 'evidencias'")

    ruta_grafica = "evidencias/resultado_comparativos.png"
    graficar_resultados(resultados, ruta_grafica)

    print("-Gráfica guardada en : 'evidencias'")
    print("\n-Pruebas completadas correctamente.")

if __name__ == "__main__":
    main()
