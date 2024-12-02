import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.optimize as opt
import Parte2  # Importamos tu archivo Parte2.py

# Función para generar una lista de monedas aleatorias
def generar_monedas(n):
    return np.random.randint(1, 100, size=n)

# Función para medir el tiempo de ejecución del algoritmo
def medir_tiempo(n_values):
    tiempos = []
    for n in n_values:
        coins = generar_monedas(n)
        # Medimos el tiempo de ejecución de juego_monedas
        start_time = time.perf_counter()
        Parte2.juego_monedas(coins)
        end_time = time.perf_counter()
        tiempos.append(end_time - start_time)
    return tiempos

# Código principal
if __name__ == "__main__":
    # Generamos valores de n desde 100 hasta 5,000 en 20 puntos
    n_values = np.linspace(100, 5000, 20, dtype=int)
    tiempos = medir_tiempo(n_values)
    
    # Gráfico de los tiempos medidos
    plt.figure(figsize=(10,6))
    plt.plot(n_values, tiempos, 'bo', label='Mediciones')
    plt.title('Tiempo de ejecución de juego_monedas (Programación Dinámica)')
    plt.xlabel('Tamaño del array (n)')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.legend()
    plt.grid(True)
    plt.savefig('imagenes/tiempos_juego_monedas_dp2.png')
    plt.show()
    
    # Ajuste por cuadrados mínimos: t = c1 * n^2 + c2
    def quadratic_func(n, c1, c2):
        return c1 * n**2 + c2
    
    # Realizamos el ajuste
    popt, pcov = opt.curve_fit(quadratic_func, n_values, tiempos)
    c1, c2 = popt
    print(f"Coeficientes de ajuste: c1 = {c1}, c2 = {c2}")
    
    # Calculamos el error cuadrático total
    residuals = tiempos - quadratic_func(n_values, *popt)
    total_squared_error = np.sum(residuals**2)
    print(f"Error cuadrático total: {total_squared_error}")
    
    # Gráfico del ajuste sobre los datos medidos
    plt.figure(figsize=(10,6))
    plt.plot(n_values, tiempos, 'bo', label='Mediciones')
    plt.plot(n_values, quadratic_func(n_values, *popt), 'r--', label='Ajuste cuadrático')
    plt.title('Ajuste cuadrático del tiempo de ejecución de juego_monedas (Programación Dinámica)')
    plt.xlabel('Tamaño del array (n)')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.legend()
    plt.grid(True)
    plt.savefig('imagenes/ajuste_juego_monedas_dp2.png')
    plt.show()
