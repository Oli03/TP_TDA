"""
Ecuación de recurrencia: max(Opt(i-2) + numero actual, Opt(i-1))
"""

def pd_parte2(vector):
    tamaño = len(vector)
    nuevo_tamaño = 0
    if tamaño == 3:
        nuevo_tamaño = 6
    elif tamaño == 4:
        nuevo_tamaño = 10
    else:
        nuevo_tamaño = 19
    solucion = [0] * (nuevo_tamaño)

    for i in range(0, tamaño):
        solucion[i] = vector[i]

    k = tamaño
    j = 0
    for i in range(tamaño, nuevo_tamaño):
        if solucion[i-k] < solucion[i-k+1]: #Saca el ultimo
            solucion[i] = solucion[i//k + j]
        else: #Saca el primero
            division = i/k
            solucion[i] = solucion[round(division)] + solucion[round(division)-2]

        j += 1
        if j == k-1:
            k -= 1
            j = 0

    return solucion

def main():
    #vector = [10, 10, 15, 10, 10, 100, 10, 10, 10, 20]
    #vector = [1, 3, 8, 6, 10, 5]
    #solucion = pd_parte2(vector, len(vector))
    #print(solucion[len(vector)])
    #print(reconstruccion(vector[:], solucion, len(vector)))
    #print(pd_parte2(vector, len(vector)))
    print(pd_parte2([1, 10, 5]))
    print(pd_parte2([2, 9, 2, 8]))
    """
    print(pd_parte2([7, 3, 2, 5, 1]))
    print(pd_parte2([4, 1, 2, 10, 3]))
    print(pd_parte2([6, 4, 8, 3, 5]))
    """

main()
