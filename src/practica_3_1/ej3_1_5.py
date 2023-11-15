"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""

from src.borrar_consola import borrar_consola

def hacer_lista():
    return list(range(1, 11))

def lista_alreves(lista):
    lista.reverse()
    return lista

def mostrar_lista(lista:list, separador:str = ", "):
    for i in range(len(lista)):
        if i != len(lista)-1 : 
            print(lista[i], end = separador)
        else:
            print(lista[i])
    return 
"""

def mostrar_lista(lista:list, separador:str = ", "):
    for i in range(len(lista) -1, -1, -1):
        if i != 0 : 
            print(lista[i], end = separador)
        else:
            print(lista[i])

def mostrar_lista(lista:list, separador:str = ", "):
    for i in range(-1, -len(lista) -1, -1):
        if i != -len(lista) : 
            print(lista[i], end = separador)
        else:
            print(lista[i])

"""

def main():
    borrar_consola()
    lista = hacer_lista()
    lista_sin = lista_alreves(lista)

    mostrar_lista(lista_sin)

    
    #Para imprimir con caracteres entre numeros en la lista ", ".join(lista), **SOLO PARA STRING, NO PARA NUMEROS**

if __name__ == "__main__":
    main()