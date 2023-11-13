"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

def pedir_num():
    
    numeros = input("Ingresa los números ganadores de la lotería primitiva separados por espacio: ")
    lista_num = [int(numeros.split())]
    lista_num.sort()
    
    return lista_num

def dar_lista(lista_num):
    serie = ""
    print("Los números ganadores de la lotería primitiva son: \n")
    for num in lista_num:
        serie += f"\n {num} \n"
    return serie

def main():
    lista_num = pedir_num()
    serie = dar_lista(lista_num)

    print(serie)


if __name__ == "__main__":
    main()