"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""
from src.borrar_consola import borrar_consola

def pedir_asig():
    asignaturas = input("Ingresa una serie de asignaturas separadas por espacio: ")
    lista_asig = asignaturas.split()
    return lista_asig

def pedir_nota(lista_asig):
    lista_not = []
    for asignatura in lista_asig:
        while True:
            try:
                nota = float(input(f"Ingrese la nota para {asignatura}: "))
                if 0 <= nota <= 10:
                    lista_not.append(nota)
                    break
                else:
                    print("¡Error! La nota debe estar en el rango de 0 a 10.")
            except ValueError:
                print("¡Error! Ingrese un valor numérico válido.")
    return lista_not

def asignaturas_a_repetir(lista_asig, lista_not, nota_minima=5.0):
    asignaturas_repetir = [asig for asig, nota in zip(lista_asig, lista_not) if nota < nota_minima]
    return asignaturas_repetir

def main():
    borrar_consola()

    lista_asig = pedir_asig()
    lista_not = pedir_nota(lista_asig)

    asignaturas_repetir = asignaturas_a_repetir(lista_asig, lista_not)

    if asignaturas_repetir:
        print("\nDebes repetir las siguientes asignaturas:")
        for asignatura in asignaturas_repetir:
            print(asignatura)
    else:
        print("\n¡Felicidades! Has aprobado todas las asignaturas.")

if __name__ == "__main__":
    main()