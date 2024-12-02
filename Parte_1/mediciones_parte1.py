import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.optimize as opt

# Definición del algoritmo juego_monedas
def juego_monedas(coins):
    """
    Función que simula el juego de las monedas entre Sophia y Mateo.
    Sophia siempre elige la moneda de mayor valor para sí misma y la de menor valor para Mateo.
    """
    i = 0
    j = len(coins) - 1
    S_Sophia = 0
    S_Mateo = 0
    while i <= j:
        # Turno de Sophia
        if coins[i] >= coins[j]:
            S_Sophia += coins[i]
            i += 1
        else:
            S_Sophia += coins[j]
            j -= 1
        if i > j:
            break
        # Turno de Mateo
        if coins[i] <= coins[j]:
            S_Mateo += coins[i]
            i += 1
        else:
            S_Mateo += coins[j]
            j -= 1
    return S_Sophia, S_Mateo

# Función para generar una lista de monedas aleatorias
def generar_monedas(n):
    return np.random.randint(1, 100, size=n)

# Función para medir el tiempo de ejecución del algoritmo
def medir_tiempo(n_values):
    tiempos = []
    for n in n_values:
        coins = generar_monedas(n)
        start_time = time.perf_counter()
        juego_monedas(coins)
        end_time = time.perf_counter()
        tiempos.append(end_time - start_time)
    return tiempos

# Código principal
if __name__ == "__main__":
    # Generamos valores de n desde 100 hasta 1,000,000 en 20 puntos
    n_values = np.linspace(100, 1_000_000, 20, dtype=int)
    tiempos = medir_tiempo(n_values)
    
    # Gráfico de los tiempos medidos
    plt.figure(figsize=(10,6))
    plt.plot(n_values, tiempos, 'bo', label='Mediciones')
    plt.title('Tiempo de ejecución de juego_monedas')
    plt.xlabel('Tamaño del array (n)')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.legend()
    plt.grid(True)
    plt.savefig('imagenes/tiempos_juego_monedas.png')
    plt.show()
    
    # Ajuste por cuadrados mínimos: t = c1 * n + c2
    def linear_func(n, c1, c2):
        return c1 * n + c2
    
    # Realizamos el ajuste
    popt, pcov = opt.curve_fit(linear_func, n_values, tiempos)
    c1, c2 = popt
    print(f"Coeficientes de ajuste: c1 = {c1}, c2 = {c2}")
    
    # Calculamos el error cuadrático total
    residuals = tiempos - linear_func(n_values, *popt)
    total_squared_error = np.sum(residuals**2)
    print(f"Error cuadrático total: {total_squared_error}")
    
    # Gráfico del ajuste sobre los datos medidos
    plt.figure(figsize=(10,6))
    plt.plot(n_values, tiempos, 'bo', label='Mediciones')
    plt.plot(n_values, linear_func(n_values, *popt), 'r--', label='Ajuste lineal')
    plt.title('Ajuste lineal del tiempo de ejecución de juego_monedas')
    plt.xlabel('Tamaño del array (n)')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.legend()
    plt.grid(True)
    plt.savefig('imagenes/ajuste_juego_monedas.png')
    plt.show()
