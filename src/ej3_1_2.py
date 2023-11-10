"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.
"""

def pedir_asig():

    asignaturas = input("Ingresa una serie de asignaturas separados por espacio: ")
    lista_asig = asignaturas.split()
    return lista_asig


def main():
    lista_asig = pedir_asig()
    for asig in lista_asig:
        print(f"Yo estudio {asig} \n")


if __name__ == "__main__":
    main()