import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.optimize as opt
import Parte3  # Importamos tu archivo Parte3.py

# Función para generar una instancia aleatoria del problema de la Batalla Naval
def generar_instancia_batalla_naval(n):
    # Generamos demandas aleatorias para filas y columnas
    demandas_filas = np.random.randint(0, n+1, size=n)
    demandas_columnas = np.random.randint(0, n+1, size=n)
    
    # Generamos una lista de largos de barcos
    max_ship_length = min(n, 5)  # Limitamos el largo máximo de los barcos
    num_ships = n  # Asumimos que el número de barcos es proporcional a n
    largos_barcos = np.random.randint(1, max_ship_length + 1, size=num_ships)
    
    return demandas_filas.tolist(), demandas_columnas.tolist(), largos_barcos.tolist()

# Función para medir el tiempo de ejecución del algoritmo
def medir_tiempo(n_values):
    tiempos = []
    for n in n_values:
        print(f"Ejecutando para tamaño n = {n}")
        demandas_filas, demandas_columnas, largos_barcos = generar_instancia_batalla_naval(n)
        # Medimos el tiempo de ejecución de batalla_naval_individual
        start_time = time.perf_counter()
        Parte3.batalla_naval_individual(largos_barcos, demandas_filas, demandas_columnas)
        end_time = time.perf_counter()
        tiempos.append(end_time - start_time)
    return tiempos

# Código principal
if __name__ == "__main__":
    # Dado que el problema es NP-Completo y el algoritmo es de backtracking,
    # limitamos los tamaños para evitar tiempos de ejecución excesivos
    n_values = range(2, 12)  # Desde tamaño 2 hasta 11
    tiempos = medir_tiempo(n_values)
    
    # Gráfico de los tiempos medidos
    plt.figure(figsize=(10,6))
    plt.plot(n_values, tiempos, 'bo-', label='Mediciones')
    plt.title('Tiempo de ejecución de batalla_naval_individual (Backtracking)')
    plt.xlabel('Tamaño del tablero (n)')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.legend()
    plt.grid(True)
    plt.savefig('imagenes/tiempos_batalla_naval_backtracking.png')
    plt.show()
    
    # Intentamos ajustar los tiempos a una función exponencial: t = a * exp(b * n)
    def exponential_func(n, a, b):
        return a * np.exp(b * n)
    
    n_values_array = np.array(list(n_values))
    tiempos_array = np.array(tiempos)
    
    # Filtramos los tiempos mayores a cero para evitar problemas con el logaritmo
    non_zero_indices = tiempos_array > 0
    n_values_array = n_values_array[non_zero_indices]
    tiempos_array = tiempos_array[non_zero_indices]
    
    # Realizamos el ajuste
    popt, pcov = opt.curve_fit(exponential_func, n_values_array, tiempos_array, p0=(1e-6, 0.5))
    a, b = popt
    print(f"Coeficientes de ajuste: a = {a}, b = {b}")
    
    # Calculamos el error cuadrático total
    residuals = tiempos_array - exponential_func(n_values_array, *popt)
    total_squared_error = np.sum(residuals**2)
    print(f"Error cuadrático total: {total_squared_error}")
    
    # Gráfico del ajuste sobre los datos medidos
    plt.figure(figsize=(10,6))
    plt.plot(n_values, tiempos, 'bo', label='Mediciones')
    n_fit = np.linspace(min(n_values), max(n_values), 100)
    plt.plot(n_fit, exponential_func(n_fit, *popt), 'r--', label='Ajuste exponencial')
    plt.title('Ajuste exponencial del tiempo de ejecución de batalla_naval_individual (Backtracking)')
    plt.xlabel('Tamaño del tablero (n)')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.legend()
    plt.grid(True)
    plt.savefig('imagenes/ajuste_batalla_naval_backtracking.png')
    plt.show()
