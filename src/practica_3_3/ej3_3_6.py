"""
Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}

1. Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
2. Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.

"""
from src.borrar_consola import borrar_consola

def guardar_abecedario():
    return set(map(chr, range(97, 123)))

def main():
    borrar_consola()

    abecedario = guardar_abecedario()

    vocales = {'a', 'e', 'i', 'o', 'u'}
    print("Vocales          => ", vocales)

    consonantes = abecedario - vocales
    print("Consonantes      => ", consonantes)

    letras_comunes = vocales | consonantes
    print("Letras comunes   => ", letras_comunes)



if __name__ == "__main__":
    main()