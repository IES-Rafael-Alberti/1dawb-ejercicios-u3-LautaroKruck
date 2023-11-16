"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""
from src.borrar_consola import borrar_consola

def pedir_palabra():
    return input("Introduce una palabra: ")

def contar_vocales(palabra):
    vocales = "aeiou"
    conteo = {vocal: 0 for vocal in vocales}

    for letra in palabra:
        if letra.lower() in vocales:
            conteo[letra.lower()] += 1

    return conteo

def mostrar_cantidad(conteo):
    serie = ""
    for vocal, cantidad in conteo.items():
        if cantidad > 1:
            serie += f"La letra {vocal} aparece {cantidad} veces.\n"
        elif cantidad == 1:
            serie += f"La letra {vocal} aparece {cantidad} vez.\n"
        else:
            serie += f"La letra {vocal} no aparece ninguna vez.\n"
    
    return serie

def main():
    borrar_consola()      

    palabra = pedir_palabra()
    conteo = contar_vocales(palabra)
    
    print(mostrar_cantidad(conteo))

if __name__ == "__main__":
    main()  