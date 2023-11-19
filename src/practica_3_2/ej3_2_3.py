"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	    Precio
Plátano	    1.35
Manzana	    0.80
Pera	    0.85
Naranja	    0.70
"""
from src.borrar_consola import borrar_consola

def pedir_fruta():
    fruta = input("Introduce una fruta: ")
    return fruta.title()

def pedir_kilos():
    while True:
        kilos_input = input("Introduce el número de kilos: ")
        try:
            kilos = float(kilos_input)
            if kilos >= 0.1:
                return kilos
            else:
                print("Por favor, introduce un número no negativo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def comprobar_fruta(fruta, d):
    return fruta in d

def calcular_precio(kilos, precio):
    return kilos * precio

def main():
    borrar_consola()
    d = {'Platano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
    fruta = pedir_fruta()
    kilos = pedir_kilos()

    if comprobar_fruta(fruta, d):
        precio = d[fruta]
        precio_total = calcular_precio(kilos, precio)

        print(f"El precio de {kilos} kilos de {fruta} es: {precio_total:.2f} euros")
    else:
        print("La fruta que ha introducido no está en el diccionario.")

if __name__ == "__main__":
    main()