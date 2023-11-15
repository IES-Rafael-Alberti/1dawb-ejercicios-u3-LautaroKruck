"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""

from src.borrar_consola import borrar_consola

def pedir_asig():
    asignaturas = input("Ingresa una serie de asignaturas separadas por espacio: ")
    lista_asig = asignaturas.split()
    return lista_asig

def dar_lista(lista_asig):
    serie = ""
    for asig in lista_asig:
        serie += f"{asig}-"
    return serie

def main():
    borrar_consola()
    lista_asig = pedir_asig()
    serie = dar_lista(lista_asig)
    print(serie[:-1])

if __name__ == "__main__":
    main()