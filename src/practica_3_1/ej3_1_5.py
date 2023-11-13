"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""

def hacer_lista():
    
    lista = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ]
    
    return lista

def lista_alreves(lista):
    lista_final = reverse(lista)
    return lista_final

def main():
    lista = hacer_lista()   
    print(lista_alreves(lista))


if __name__ == "__main__":
    main()