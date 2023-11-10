"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""

def pedir_asig():

    asignaturas = input("Ingresa una serie de asignaturas separados por espacio: ")
    lista_asig = asignaturas.split()
    return lista_asig

def pedir_nota():

    notas = input("Ingresa las notas de las asignaturas anteriores separadas por espacio: ")
    lista_not = notas.split()
    return lista_not


def main():
    lista_asig = pedir_asig()
    cont = len(lista_asig)
    lista_not = pedir_nota()
    lista = lista_asig + lista_not


    for asig in lista:
        print(f"En {asig} has sacado {asig + cont} \n")
    

        

if __name__ == "__main__":
    main()