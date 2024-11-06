import sys

def juego_monedas(coins):
    """
    Función que simula el juego de las monedas entre Sophia y Mateo.
    Sophia siempre elige la moneda de mayor valor para sí misma y la de menor valor para Mateo.
    Parámetros:
    - coins: Lista de enteros que representa los valores de las monedas en fila.
    Retorna:
    - S_Sophia: Suma total acumulada por Sophia.
    - S_Mateo: Suma total acumulada por Mateo.
    - elecciones: Lista de elecciones en el orden solicitado.
    """
    # Inicialización de índices y sumas acumuladas
    i = 0                      # Índice inicial
    j = len(coins) - 1         # Índice final
    S_Sophia = 0               # Suma total de Sophia
    S_Mateo = 0                # Suma total de Mateo
    elecciones = []            # Lista para registrar las elecciones

    # Mientras queden monedas por elegir
    while i <= j:
        # Turno de Sophia
        if coins[i] >= coins[j]:
            S_Sophia += coins[i]
            elecciones.append(f"Primera moneda para Sophia")
            i += 1
        else:
            S_Sophia += coins[j]
            elecciones.append(f"Última moneda para Sophia")
            j -= 1

        # Verificamos si ya no quedan monedas después del turno de Sophia
        if i > j:
            break

        # Turno de Mateo (Sophia elige por él)
        if coins[i] <= coins[j]:
            S_Mateo += coins[i]
            elecciones.append(f"Primera moneda para Mateo")
            i += 1
        else:
            S_Mateo += coins[j]
            elecciones.append(f"Última moneda para Mateo")
            j -= 1

    return S_Sophia, S_Mateo, elecciones

# Función para leer los datos del archivo
def main():
    # Verifica que se pase un argumento con el nombre del archivo
    if len(sys.argv) < 2:
        print("Por favor, proporciona el nombre del archivo.")
        return

    # Acá obtenemos el nombre del archivo desde los argumentos pasados por línea de comandos
    file_path = sys.argv[1]

    # Leemos el archivo
    try:
        with open(file_path, 'r') as file:
            # Ignoramos la primera línea que contiene el comentario
            next(file)
            data = file.read().strip()
        
        # Convertimos los valores en una lista de enteros
        coins = list(map(int, data.split(";")))

        # Ejecutamos el juego
        suma_sophia, suma_mateo, elecciones = juego_monedas(coins)

        # Formatear y mostrar el resultado
        print("; ".join(elecciones))
        print(f"Ganancia de Sophia: {suma_sophia}")
        print(f"Ganancia de Mateo: {suma_mateo}")
    except FileNotFoundError:
        print(f"El archivo '{file_path}' no fue encontrado.")

# Ejecutar el programa
main()