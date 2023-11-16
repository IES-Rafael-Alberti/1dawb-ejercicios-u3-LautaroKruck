"""
Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.
"""
from src.borrar_consola import borrar_consola

def guardar_precios():
    return (50, 75 ,46 ,22 ,80 ,65 ,8 )

def precio_menor(lista):
    return min(lista)

def precio_mayor(lista):
    return max(lista)

def main():
    borrar_consola()

    lista = guardar_precios()
    menor = precio_menor(lista)
    mayor = precio_mayor(lista)

    print(f"El precio menor es {menor} y el mayor {mayor}.")

if __name__ == "__main__":
    main()  