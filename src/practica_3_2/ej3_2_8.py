"""
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""
from src.borrar_consola import borrar_consola

def pedir_palabra_esp():
    pal_esp = input("Introduce una palabra en español (x para salir): ")
    return pal_esp.lower()

def pedir_palabra_ing():
    pal_ing = input("Introduce la traducción en inglés: ")
    return pal_ing.lower()

def pedir_frase():
    frase = input("Introduce una frase en español: ")
    return frase.lower().split()

def guardar_palabras(traduccion, pal_esp, pal_ing):
    traduccion[pal_esp] = pal_ing
    return traduccion

def traducir_frase(traduccion, frase):
    traduccion_frase = [traduccion.get(palabra, palabra) for palabra in frase]
    return ' '.join(traduccion_frase)

def main():
    borrar_consola()

    traduccion = {}
    pal_esp = pedir_palabra_esp()
    
    while pal_esp != "x":
        pal_ing = pedir_palabra_ing()
        traduccion = guardar_palabras(traduccion, pal_esp, pal_ing)
        pal_esp = pedir_palabra_esp()

    frase = pedir_frase()
    frase_traducida = traducir_frase(traduccion, frase)

    print("Frase traducida:", frase_traducida)

if __name__ == "__main__":
    main()
