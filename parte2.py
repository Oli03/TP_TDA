"""

Ecuación de recurrencia: max(OPT(sin el primer elemento) + primer elemento, OPT(sin el ultimo elemento) + ultimo elemento)

Ejemplo de la ecuación de recurrencia (termina en la linea 254):

[4, 2, 7, 5, 6, 1, 9, 0, 3, 8] max(opt(sin el 4) + 4, opt(sin el 8) + 8) Sophia: 0, Mateo: 0

    Sophia saco el 4
    [2, 7, 5, 6, 1, 9, 0, 3, 8] Mateo saca el 8
    [2, 7, 5, 6, 1, 9, 0, 3] max(opt(sin el 2) + 2, opt(sin el 3) + 3) Sophia: 4, Mateo: 8

        Sophia saco el 2
        [7, 5, 6, 1, 9, 0, 3] Mateo saca el 7
        [5, 6, 1, 9, 0, 3] max(opt(sin el 5) + 5, opt(sin el 3) + 3) Sophia: 6, Mateo: 15

            Sophia saco el 5
            [6, 1, 9, 0, 3] Mateo saco el 6
            [1, 9, 0, 3] max(opt(sin el 1) + 1, opt(sin el 3) + 3) Sophia: 11, Mateo: 21

                Sophia saco el 1
                [9, 0, 3] Mateo saco el 9
                [0, 3] max(opt(sin el 0) + 0, opt(sin el 3)) Sophia: 12, Mateo: 30

                    Sophia saco el 0
                    [3] Mateo saco el 3
                    [] Sophia: 12, Mateo: 33

                    Sophia saco el 3
                    [0] Mateo saco el 0
                    [] Sophia: 15, Mateo: 30

                Sophia saco el 3
                [1, 9, 0] Mateo saco el 1
                [9, 0] max(opt(sin el 9) + 9, opt(sin el 0) + 0) Sophia: 14, Mateo: 22

                    Sophia saco el 9
                    [0] Mateo saco el 0
                    [] Sophia: 23, Mateo: 22

                    Sophia saco el 0
                    [9] Mateo saco el 9
                    [] Sophia: 14, Mateo: 31

            Sophia saco el 3
            [5, 6, 1, 9, 0] Mateo saco el 5
            [6, 1, 9, 0] max(opt(sin el 6) + 6, opt(sin el 0) + 0) Sophia: 9, Mateo: 20

                Sophia saco el 6
                [1, 9, 0] Mateo saco el 1
                [9, 0] max(opt(sin el 9) + 9, opt(sin el 0) + 0) Sophia: 15, Mateo: 21

                    Sophia saco el 9
                    [0] Mateo saco el 0
                    [] Sophia: 24, Mateo: 21

                    Sophia saco el 0
                    [9] Mateo saco el 9
                    [] Sophia: 15, Mateo: 30

                Sophia saco el 0
                [6, 1, 9] Mateo saco el 9
                [6, 1] max(opt(sin el 6) + 6, opt(sin el 1) + 1) Sophia: 9, Mateo: 29

                    Sophia saco el 6
                    [1] Mateo saco el 1
                    [] Sophia: 15, Mateo: 30

                    Sophia saco el 1
                    [6] Mateo saco el 6
                    [] Sophia: 10, Mateo: 35

        Sophia saco el 3
        [2, 7, 5, 6, 1, 9, 0] Mateo saco el 2
        [7, 5, 6, 1, 9, 0] max(opt(sin el 7) + 7, opt(sin el 0) + 0) Sophia: 7, Mateo: 10

            Sophia saco el 7
            [5, 6, 1, 9, 0] Mateo saco el 5
            [6, 1, 9, 0] max(opt(sin el 6) + 6, opt(sin el 0) + 0) Sophia: 14, Mateo: 15

                Sophia saco el 6
                [1, 9, 0] Mateo saco el 1
                [9, 0] max(opt(sin el 9) + 9, opt(sin el 0) + 0) Sophia: 20, Mateo: 16

                    Sophia saco el 9
                    [0] Mateo saco el 0
                    [] Sophia: 29, Mateo: 16

                    Sophia saco el 0
                    [9] Mateo saco el 9
                    [] Sophia: 20, Mateo: 25

                Sophia saco 0
                [6, 1, 9] Mateo saco el 9
                [6, 1] Sophia: 14, Mateo: 24

                    Sophia saco el 6
                    [1] Mateo saco el 1
                    [] Sophia: 20, Mateo: 25

                    Sophia saco el 1
                    [6] Mateo saco el 6
                    [] Sophia: 15, Mateo: 30

            Sophia saco el 0
            [7, 5, 6, 1, 9] Mateo saco el 9
            [7, 5, 6, 1] max(opt(sin el 7) + 7, opt(sin el 1) + 1) Sophia: 7, Mateo: 19

                Sophia saco el 7
                [5, 6, 1] Mateo saco el 5
                [6, 1] max(opt(sin el 6) + 6, opt(sin el 1) + 1) Sophia: 14, Mateo: 24

                    Sophia saco el 6
                    [1] Mateo saco el 1
                    [] Sophia: 20, Mateo: 25

                    Sophia saco el 1
                    [6] Mateo saco el 6
                    [] Sophia: 15, Mateo: 30

                Sophia saco 1
                [7, 5, 6] Mateo saco el 7
                [5, 6] max(opt(sin el 5) + 5, opt(sin el 6) + 6) Sophia: 8, Mateo: 26

                    Sophia saco el 5
                    [6] Mateo saco el 6
                    [] Sophia: 13, Mateo: 32

                    Sophia saco el 6
                    [5] Mateo saco el 5
                    [] Sophia: 14, Mateo: 31

    Sophia saco el 8
    [4, 2, 7, 5, 6, 1, 9, 0, 3] Mateo saca el 4
    [2, 7, 5, 6, 1, 9, 0, 3] max(opt(sin el 2) + 2, opt(sin el 3) + 3) Sophia: 8, Mateo: 4

        Sophia saco el 2
        [7, 5, 6, 1, 9, 0, 3] Mateo saca el 7
        [5, 6, 1, 9, 0, 3] max(opt(sin el 5) + 5, opt(sin el 3) + 3) Sophia: 10, Mateo: 11

            Sophia saco el 5
            [6, 1, 9, 0, 3] Mateo saco el 6
            [1, 9, 0, 3] max(opt(sin el 1) + 1, opt(sin el 3) + 3) Sophia: 15, Mateo: 17

                Sophia saco el 1
                [9, 0, 3] Mateo saco el 9
                [0, 3] max(opt(sin el 0) + 0, opt(sin el 3)) Sophia: 16, Mateo: 26

                    Sophia saco el 0
                    [3] Mateo saco el 3
                    [] Sophia: 16, Mateo: 29

                    Sophia saco el 3
                    [0] Mateo saco el 0
                    [] Sophia: 19, Mateo: 26

                Sophia saco el 3
                [1, 9, 0] Mateo saco el 1
                [9, 0] max(opt(sin el 9) + 9, opt(sin el 0) + 0) Sophia: 18, Mateo: 18

                    Sophia saco el 9
                    [0] Mateo saco el 0
                    [] Sophia: 27, Mateo: 18

                    Sophia saco el 0
                    [9] Mateo saco el 9
                    [] Sophia: 18, Mateo: 27

            Sophia saco el 3
            [5, 6, 1, 9, 0] Mateo saco el 5
            [6, 1, 9, 0] max(opt(sin el 6) + 6, opt(sin el 0) + 0) Sophia: 13, Mateo: 16

                Sophia saco el 6
                [1, 9, 0] Mateo saco el 1
                [9, 0] max(opt(sin el 9) + 9, opt(sin el 0) + 0) Sophia: 19, Mateo: 17

                    Sophia saco el 9
                    [0] Mateo saco el 0
                    [] Sophia: 28, Mateo: 17

                    Sophia saco el 0
                    [9] Mateo saco el 9
                    [] Sophia: 19, Mateo: 26

                Sophia saco el 0
                [6, 1, 9] Mateo saco el 9
                [6, 1] max(opt(sin el 6) + 6, opt(sin el 1) + 1) Sophia: 13, Mateo: 25

                    Sophia saco el 6
                    [1] Mateo saco el 1
                    [] Sophia: 19, Mateo: 26

                    Sophia saco el 1
                    [6] Mateo saco el 6
                    [] Sophia: 14, Mateo: 31

        Sophia saco el 3
        [2, 7, 5, 6, 1, 9, 0] Mateo saco el 2
        [7, 5, 6, 1, 9, 0] max(opt(sin el 7) + 7, opt(sin el 0) + 0) Sophia: 11, Mateo: 6

            Sophia saco el 7
            [5, 6, 1, 9, 0] Mateo saco el 5
            [6, 1, 9, 0] max(opt(sin el 6) + 6, opt(sin el 0) + 0) Sophia: 18, Mateo: 11

                Sophia saco el 6
                [1, 9, 0] Mateo saco el 1
                [9, 0] max(opt(sin el 9) + 9, opt(sin el 0) + 0) Sophia: 24, Mateo: 12

                    Sophia saco el 9
                    [0] Mateo saco el 0
                    [] Sophia: 33, Mateo: 12

                    Sophia saco el 0
                    [9] Mateo saco el 9
                    [] Sophia: 24, Mateo: 21

                Sophia saco 0
                [6, 1, 9] Mateo saco el 9
                [6, 1] Sophia: 18, Mateo: 20

                    Sophia saco el 6
                    [1] Mateo saco el 1
                    [] Sophia: 24, Mateo: 21

                    Sophia saco el 1
                    [6] Mateo saco el 6
                    [] Sophia: 19, Mateo: 26

            Sophia saco el 0
            [7, 5, 6, 1, 9] Mateo saco el 9
            [7, 5, 6, 1] max(opt(sin el 7) + 7, opt(sin el 1) + 1) Sophia: 11, Mateo: 15

                Sophia saco el 7
                [5, 6, 1] Mateo saco el 5
                [6, 1] max(opt(sin el 6) + 6, opt(sin el 1) + 1) Sophia: 18, Mateo: 20

                    Sophia saco el 6
                    [1] Mateo saco el 1
                    [] Sophia: 24, Mateo: 21

                    Sophia saco el 1
                    [6] Mateo saco el 6
                    [] Sophia: 19, Mateo: 26

                Sophia saco 1
                [7, 5, 6] Mateo saco el 7
                [5, 6] max(opt(sin el 5) + 5, opt(sin el 6) + 6) Sophia: 12, Mateo: 22

                    Sophia saco el 5
                    [6] Mateo saco el 6
                    [] Sophia: 17, Mateo: 28

                    Sophia saco el 6
                    [5] Mateo saco el 5
                    [] Sophia: 18, Mateo: 27
"""

def pd_parte2(vector, numero_actual, iteracion):
    print(f"Iteración: {iteracion}")

    if numero_actual >= 0:
        print(f"Sophia saco el {numero_actual}")

        numero_quitado = 0

        if vector[0] >= vector[len(vector)-1]:
            numero_quitado = vector.pop(0)
        else:
            numero_quitado = vector.pop()

        print(f"Mateo saco el {numero_quitado}")

    if not vector:
        return 0
    
    vector1 = vector[:]
    vector2 = vector[:]
    primer_numero = vector1.pop(0)
    ultimo_numero = vector2.pop()
    return max(pd_parte2(vector1, primer_numero, iteracion + 1) + primer_numero, pd_parte2(vector2, ultimo_numero, iteracion + 1) + ultimo_numero)

def main():
    vector = [4, 2, 7, 5, 6, 1, 9, 0, 3, 8]
    print(pd_parte2(vector, -1, 0))

main()
