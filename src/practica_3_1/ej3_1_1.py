"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""

def pedir_asig():

    asignaturas = input("Ingresa una serie de asignaturas separados por espacio: ")
    lista_asig = asignaturas.split()
    return lista_asig

def dar_lista(lista_asig):
    serie = ""
    for asig in lista_asig:
        serie += f"{asig}-"
    return serie


def main():
    lista_asig = pedir_asig()
    serie = dar_lista(lista_asig)
    print(dar_lista(serie))

if __name__ == "__main__":
    main()