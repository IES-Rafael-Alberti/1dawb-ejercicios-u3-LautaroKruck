"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""
def pedir_asig():

    asignaturas = input("Ingresa una serie de asignaturas separados por espacio: ")
    lista_asig = asignaturas.split()
    return lista_asig

def pedir_nota():

    notas = input("Ingresa las notas de las asignaturas anteriores separadas por espacio: ")
    lista_not = [float(num) for num in notas.split()]

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