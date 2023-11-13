"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.
"""
from src.practica_3_1.ej3_1_1 import pedir_asig

def dar_lista(lista_asig):
    serie = ""
    for asig in lista_asig:
        serie += f"Yo estudio {asig} \n"
    return serie

def main():
    lista_asig = pedir_asig()
    serie = dar_lista(lista_asig)
    print(serie)


if __name__ == "__main__":
    main()