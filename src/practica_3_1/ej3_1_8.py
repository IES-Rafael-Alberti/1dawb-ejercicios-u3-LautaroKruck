"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""
from src.borrar_consola import borrar_consola

def pedir_palabra():
    return input("Introduce una palabra: ")

def palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

def main():
    borrar_consola()

    palabra = pedir_palabra()
    
    if palindromo(palabra):
        print(f"{palabra} es un palíndromo.")
    else:
        print(f"{palabra} no es un palíndromo.")

if __name__ == "__main__":
    main()