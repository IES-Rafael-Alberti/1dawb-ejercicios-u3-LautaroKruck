"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

def pedir_num():
    
    numeros = input("Ingresa los números ganadores de la lotería primitiva separados por espacio: ")
    
    lista_num = [float(num) for num in numeros.split()]
    lista_num.sort()
    
    return lista_num

def guardar_num():
    print

def dar_lista(lista_num):
    serie = ""
    print("Los números ganadores de la lotería primitiva son: \n")
    cont = 1
    for num in lista_num:

        serie += f"\n {num:.0f} \n"
    return serie

def main():
    print("Introduzca los números de la lotería: \n")
    lista_num = pedir_num()
    serie = dar_lista(lista_num)

    print(serie)


if __name__ == "__main__":
    main()