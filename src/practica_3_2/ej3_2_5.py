"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""
from src.borrar_consola import borrar_consola

def cred_asigs(creditos_asigs):
    total_creditos = 0
    for asignatura, creditos in creditos_asigs.items():
        total_creditos += creditos
        print(f"{asignatura} tiene {creditos} créditos.")
    
    return total_creditos

def mostrar_total(total_creditos):
    print(f"El número total de créditos del curso es {total_creditos}.")

def main():
    borrar_consola()

    creditos_asigs = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

    total_creditos = cred_asigs(creditos_asigs)

    mostrar_total(total_creditos)

if __name__ == "__main__":
    main()
