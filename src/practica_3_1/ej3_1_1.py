"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""

def pedir_asig():

    asignaturas = input("Ingresa una serie de asignaturas separados por espacio: ")
    lista_asig = asignaturas.split()
    return lista_asig


def main():
    lista_asig = pedir_asig()
    
    print(lista_asig)

if __name__ == "__main__":
    main()