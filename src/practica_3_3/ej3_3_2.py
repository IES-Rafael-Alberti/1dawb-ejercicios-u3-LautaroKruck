"""
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria.
"""
from src.borrar_consola import borrar_consola

def pedir_alumnos_primaria(msj:str) -> list:
    alumnos_primaria = set()
    alumno = ""

    while alumno != "x" :
        alumno = input("¿Desea introducir más nombres? (Para salir introduzca x): ").lower()
        alumnos_primaria.append(alumno)
    return alumnos_primaria

def pedir_alumnos_secundaria(msj:str) -> list:
    alumnos_secundaria = set()
    alumno = ""

    while alumno != "x" :
        alumno = input("¿Desea introducir más nombres? (Para salir introduzca x): ").lower()
        alumnos_secundaria.append(alumno)
    return alumnos_secundaria

def mostrar_alumnos(ciclo: str, alumnos: set) -> str:
    print()

def main():
    borrar_consola()

    alumnos_primaria = pedir_alumnos_primaria()

    alumnos_secundaria = pedir_alumnos_secundaria()

    mostrar_alumnos("Nombres no repetidos => ", set(alumnos_primaria) | set (alumnos_secundaria))

    info = pedir_info()

    while info == "Y":
        artículo = input("Introduce el artículo: \n").title()
        lista_de_primaria = añadir_articulo(lista_de_compra, artículo)
        lista_de_secundaria = añadir_articulo(lista_de_compra, artículo)

        print(lista_de_compra)

        info = pedir_info()

    calcular_total(lista_de_compra)
    print(lista_de_compra)



if __name__ == "__main__":
    main()