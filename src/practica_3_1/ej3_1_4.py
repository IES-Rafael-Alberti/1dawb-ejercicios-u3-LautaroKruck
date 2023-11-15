"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

from src.borrar_consola import borrar_consola

def pedir_num():
    while True:
        try:
            num = int(input("Ingresa un número entre 1 y 49: "))
            if 1 <= num <= 49:
                return num
            else:
                print("**Error** Número fuera de rango.")
        except ValueError:
            print("**Error** Ingresa un número válido.")

def pedir_reintegro():
    while True:
        try:
            reintegro = int(input("Ingresa el reintegro (entre 0 y 9): "))
            if 0 <= reintegro <= 9:
                return reintegro
            else:
                print("**Error** Número fuera de rango.")
        except ValueError:
            print("**Error** Ingresa un número válido.")

def guardar_num():
    lista = []
    for i in range(6):
        num = pedir_num()
        lista.append(num)
    return sorted(lista)

def dar_lista(lista_num, reintegro):
    print("\nLos números ganadores de la lotería primitiva son:")
    for num in lista_num:
        print(num, end=' ')
    print(f"\nReintegro: {reintegro}")

def main():
    borrar_consola()
    try:
        print("Introduzca los números de la lotería: ")
        lista_num = guardar_num()
        reintegro = pedir_reintegro()
        dar_lista(lista_num, reintegro)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()