"""
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""
from src.borrar_consola import borrar_consola


def pedir_palabra_esp():
    pal_esp = input("Introduce una palabra en español: ")
    return pal_esp.lower()

def pedir_palabra_ing():
    pal_ing = input("Introduce la traducción en inglés: ")
    return pal_ing.lower()

def pedir_frase():
    frase = input("Introduce una frase en español: ")
    return frase.lower().split()

def guardar_palabras(traduccion, pal_esp ,pal_ing):
    traduccion[pal_esp] = pal_ing
    return traduccion


def main():
    borrar_consola()
    traduccion = {}


if __name__ == "__main__":
    main()

