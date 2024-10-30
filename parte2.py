"""
Se utiliza una matriz nxn
Casos base:
1) Si i y j son iguales: Opt[i][j] = vector[i]
2) Si la diferencia entre i y j es 1 o -1: Opt[i][j] = max(Opt[i][j-1], Opt[i+1][j])

Ecuación de recurrencia:
Opt[i][j] = max(vector[i] + min(Opt[i+1][j-1], Opt[i][j-2]), vector[i-2] + min(Opt[i+1][j-1], Opt[i+2][j]))
"""

def pd_parte2(vector):
    n = len(vector)
    puntajes = [[0] * n for _ in range(n)]

    #Caso base 1)
    for i in range(0, n):
        puntajes[i][i] = vector[i]

    #Caso base 2)
    for i in range(0, n-1):
        puntajes[i][i+1] = max(vector[i], vector[i+1])

    #Aplicación de la ecuación de recurrencia
    i = 0
    j = 2
    tope = n//2
    for _ in range(0, n+1):
        if puntajes[0][n-1] != 0:
            return puntajes
    
        if n % 2 != 0:
            if i > tope:
                j -= (i-1)
                i = 0
                tope -= 1
        else:
            if i == tope:
                j -= (i-1)
                i = 0
                tope -= 1

        tomar_ultimo_elemento = vector[j] + min(puntajes[i+1][j-1], puntajes[i][j-2])
        tomar_primer_elemento = vector[i] + min(puntajes[i+1][j-1], puntajes[i+2][j])
        puntajes[i][j] = max(tomar_ultimo_elemento, tomar_primer_elemento)

        i += 1
        j += 1

    return puntajes


def main():
    print(pd_parte2([1, 10, 5]))
    print(pd_parte2([2, 9, 2, 8]))
    print(pd_parte2([7, 3, 2, 5, 1]))
    print(pd_parte2([4, 1, 2, 10, 3]))
    print(pd_parte2([6, 4, 8, 3, 5]))

main()
