"""
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

1. Crea un conjunto pares que contenga los números pares del conjunto numeros.
2. Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
3. Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
"""
from src.borrar_consola import borrar_consola


def main():
    borrar_consola()

    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    pares = 
    print("Nombres no repetidos => ", pares)

    multiplos_de_tres = 
    print("Nombres que se repiten => ", multiplos_de_tres)
    
    pares_y_multiplos_de_tres = pares & multiplos_de_tres
    print("Frutas que están en frutas1 pero no en frutas2 => ", pares_y_multiplos_de_tres)  


if __name__ == "__main__":
    main()