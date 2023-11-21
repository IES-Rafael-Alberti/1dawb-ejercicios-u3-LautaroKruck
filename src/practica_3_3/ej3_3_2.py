"""
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria.
"""
from src.borrar_consola import borrar_consola

def pedir_alumnos_nivel(msj: str) -> set:
    alumnos_nivel = set()
    alumno = ""

    while alumno.lower() != "x":
        alumno = input(msj).capitalize()
        if alumno.lower() != "x":
            alumnos_nivel.add(alumno)

    return alumnos_nivel

def mostrar_alumnos(titulo: str, alumnos: set) -> None:
    print(titulo)
    alumnos_str = " - ".join(alumnos)
    print(alumnos_str)
    print()

def main():
    borrar_consola()

    alumnos_primaria = pedir_alumnos_nivel("Introduce el nombre de un alumno de primaria (Para salir introduce 'x'): ")

    alumnos_secundaria = pedir_alumnos_nivel("Introduce el nombre de un alumno de secundaria (Para salir introduce 'x'): ")

    mostrar_alumnos("Nombres no repetidos => ", alumnos_primaria | alumnos_secundaria)

    mostrar_alumnos("Nombres que se repiten => ", alumnos_primaria & alumnos_secundaria)

    mostrar_alumnos("Nombres de primaria no repetidos en secundaria => ", alumnos_primaria - alumnos_secundaria)

    print("¿Todos los nombres de primaria están incluidos en secundaria? ", alumnos_primaria.issubset(alumnos_secundaria))

if __name__ == "__main__":
    main()
