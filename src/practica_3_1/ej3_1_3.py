"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""
from src.ej3_1_1 import pedir_asig

def pedir_nota():

    notas = input("Ingresa las notas de las asignaturas anteriores separadas por espacio: ")
    lista_not = notas.split()
    return lista_not


def dar_lista(lista_asig, lista_not):
    serie = ""
    for i in range (0 , len(lista_not)):
        serie += f"\n En {lista_asig[i]} has sacado {lista_not[i]} \n"
    return serie


def main():
    lista_asig = pedir_asig()
    lista_not = pedir_nota()
    serie = dar_lista(lista_asig, lista_not)

    print(serie)


if __name__ == "__main__":
    main()