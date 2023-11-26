"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""
from src.practica_3_1.ej3_1_1 import pedir_asig
from src.borrar_consola import borrar_consola

def pedir_nota(lista_asig):
    lista_not = []
    for asignatura in lista_asig:
        nota = float(input(f"Ingrese la nota para {asignatura}: "))
        lista_not.append(nota)
    return lista_not

def dar_lista(lista_asig, lista_not):
    serie = ""
    for i in range(len(lista_not)):
        serie += f"\n En {lista_asig[i]} has sacado {lista_not[i]} \n"
    return serie

def main():
    borrar_consola()
    lista_asig = pedir_asig()
    lista_not = pedir_nota(lista_asig)
    serie = dar_lista(lista_asig, lista_not)

    print(serie)

if __name__ == "__main__":
    main()