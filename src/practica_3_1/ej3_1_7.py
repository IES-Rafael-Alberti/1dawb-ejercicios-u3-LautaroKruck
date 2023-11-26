"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""

from src.borrar_consola import borrar_consola

def guardar_abecedario():
    return list(map(chr, range(97, 123)))

def eliminar_letras(lista):
    i = len(lista) - 1
    while i >= 0:
        if (i + 1) % 3 == 0:
            del lista[i]
        i -= 1
    return lista

def main():
    borrar_consola()

    lista = guardar_abecedario()
    lista_resultante = eliminar_letras(lista)
    print(lista_resultante)
    
    

if __name__ == "__main__":
    main()