"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""

from src.borrar_consola import borrar_consola

def guardar_abecedario():
    return list(map(chr, range(97, 123)))

def eliminar_letras(lista):
    cont = 0
    max = len(lista) - 1 
    while cont <= max:
        if cont % 3 == 0:
            del lista[cont]
            max -= 1
            cont +=1

    return lista


def main():
    lista = guardar_abecedario()
    eliminar_letras(lista)
    print(lista)
    
    borrar_consola()


if __name__ == "__main__":
    main()