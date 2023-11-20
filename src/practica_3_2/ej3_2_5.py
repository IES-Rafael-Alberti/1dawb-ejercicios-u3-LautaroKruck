"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""
from src.borrar_consola import borrar_consola

def main():
    borrar_consola()

    cred_asigs = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

    print()
    total_cred = 0
    for asig , cred in cred_asigs.items():

        total_cred += cred
        print (f"{asig} tiene {cred} créditos.")

    print(f"El número totl de creditos del curso es {total_cred}.")

if __name__ == "__main__":
    main()