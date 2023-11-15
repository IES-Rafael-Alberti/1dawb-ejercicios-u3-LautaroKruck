"""
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
"""


def prod_vectorial(v1 : tuple , v2 : tuple) -> tuple:
    l3 =[]

    cont = 0
    while cont < len(v1):
        l3.append(v1[cont] * v2[cont])
        cont += 1

    return tuple(l3)

"""
def prod_vectorial(v1 : tuple , v2 : tuple) -> tuple:
    l3 =[]

    for i in range(len(v1))
        l3.append(v1[i] * v2[i])

    return tuple(l3)
"""

"""
def prod_vectorial(v1 : tuple , v2 : tuple) -> tuple:
    l3 = tuple(v1[i] * v2[i] for i in range(len(v1)))

    return tuple(l3)
"""


def main():
    v1 = (-1 , 4 , 2)
    v2 = (2 , 2 , 2)

    v3 = prod_vectorial(v1 , v2)

    print(v3)


if __name__ == "__main__":
    main()