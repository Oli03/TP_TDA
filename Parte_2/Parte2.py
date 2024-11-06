import sys

def juego_monedas(coins):
    """
    Función que simula el juego de las monedas entre Sophia y Mateo utilizando programación dinámica.
    Sophia busca maximizar su ganancia sabiendo que Mateo siempre elige la moneda de mayor valor
    entre las opciones disponibles en sus turnos.
    Parámetros:
    - coins: Lista de enteros que representa los valores de las monedas en fila.
    Retorna:
    - S_Sophia: Suma total acumulada por Sophia.
    - S_Mateo: Suma total acumulada por Mateo.
    - elecciones: Lista de elecciones en el orden solicitado.
    """
    n = len(coins)
    # Matrices para programación dinámica y para rastrear las elecciones
    DP = [[-1] * n for _ in range(n)]       # Matriz para almacenar las ganancias máximas de Sophia
    move = [[None] * n for _ in range(n)]   # Matriz para almacenar las elecciones de Sophia ('i' o 'j')

    # Función recursiva para calcular la ganancia máxima de Sophia
    def F(i, j):
        if i > j:
            return 0
        if DP[i][j] != -1:
            return DP[i][j]
        if i == j:
            DP[i][j] = coins[i]
            move[i][j] = 'i'
            return DP[i][j]

        # Opción 1: Sophia elige la moneda en posición i
        # Simulamos la elección de Mateo
        if i + 1 <= j:
            if coins[i + 1] >= coins[j]:
                # Mateo elige la moneda en posición i + 1
                new_i, new_j = i + 2, j
            else:
                # Mateo elige la moneda en posición j
                new_i, new_j = i + 1, j - 1
        else:
            # No hay monedas para que Mateo elija
            new_i, new_j = i + 1, j

        option1 = coins[i] + F(new_i, new_j)

        # Opción 2: Sophia elige la moneda en posición j
        # Simulamos la elección de Mateo
        if i <= j - 1:
            if coins[i] >= coins[j - 1]:
                # Mateo elige la moneda en posición i
                new_i2, new_j2 = i + 1, j - 1
            else:
                # Mateo elige la moneda en posición j - 1
                new_i2, new_j2 = i, j - 2
        else:
            # No hay monedas para que Mateo elija
            new_i2, new_j2 = i, j - 1

        option2 = coins[j] + F(new_i2, new_j2)

        # Elegimos la mejor opción para Sophia
        if option1 >= option2:
            DP[i][j] = option1
            move[i][j] = 'i'
        else:
            DP[i][j] = option2
            move[i][j] = 'j'

        return DP[i][j]

    # Ejecutamos la función desde el estado inicial
    total_sophia = F(0, n - 1)

    # Reconstruimos las elecciones de Sophia y Mateo
    elecciones = []
    i, j = 0, n - 1
    S_Sophia, S_Mateo = 0, 0

    while i <= j:
        if move[i][j] == 'i':
            # Sophia elige la moneda en posición i
            S_Sophia += coins[i]
            elecciones.append(f"Primera moneda para Sophia")
            # Turno de Mateo
            if i + 1 <= j:
                if coins[i + 1] >= coins[j]:
                    # Mateo elige la moneda en posición i + 1
                    S_Mateo += coins[i + 1]
                    elecciones.append(f"Primera moneda para Mateo")
                    i += 2
                else:
                    # Mateo elige la moneda en posición j
                    S_Mateo += coins[j]
                    elecciones.append(f"Última moneda para Mateo")
                    i += 1
                    j -= 1
            else:
                # No hay monedas para Mateo
                i += 1
        else:
            # Sophia elige la moneda en posición j
            S_Sophia += coins[j]
            elecciones.append(f"Última moneda para Sophia")
            # Turno de Mateo
            if i <= j - 1:
                if coins[i] >= coins[j - 1]:
                    # Mateo elige la moneda en posición i
                    S_Mateo += coins[i]
                    elecciones.append(f"Primera moneda para Mateo")
                    i += 1
                    j -= 1
                else:
                    # Mateo elige la moneda en posición j - 1
                    S_Mateo += coins[j - 1]
                    elecciones.append(f"Última moneda para Mateo")
                    j -= 2
            else:
                # No hay monedas para Mateo
                j -= 1

    return S_Sophia, S_Mateo, elecciones

# Función para leer los datos del archivo y ejecutar el programa
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
            # Ignoramos la primera línea si contiene un comentario
            first_line = file.readline()
            if first_line.startswith("#"):
                data = file.read().strip()
            else:
                data = first_line.strip() + file.read().strip()
        
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

# Ejecutamos el programa
if __name__ == "__main__":
    main()
