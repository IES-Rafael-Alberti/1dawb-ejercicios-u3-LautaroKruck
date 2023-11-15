"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""

from src.borrar_consola import borrar_consola

def hacer_lista():
    return list(range(1, 11))

def lista_alreves(lista):
    lista.reverse()
    return lista

def main():
    borrar_consola()
    lista = hacer_lista()
    print(lista_alreves(lista))

if __name__ == "__main__":
    main()