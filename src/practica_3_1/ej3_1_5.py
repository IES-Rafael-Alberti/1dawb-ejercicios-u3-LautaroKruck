"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""

def pedir_num():
    
    numeros = input("Ingresa los números ganadores de la lotería primitiva separados por espacio: ")
    lista_num = [float(num) for num in numeros.split()]
    lista_num.reverse()
    
    return lista_num

def dar_lista(lista_num):
    serie = ""
    for num in lista_num:
        serie += f"Yo estudio {num} \n"
    return serie

def main():
    lista_num = pedir_num()
    serie = dar_lista(lista_num)
    print(serie)


if __name__ == "__main__":
    main()