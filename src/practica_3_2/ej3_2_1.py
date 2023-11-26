"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""
from src.borrar_consola import borrar_consola

def pedir_divisa():
    divisa = input("Introduce una divisa: ")
    return divisa.title()

def comprobar_divisa(divisa, d):
    if divisa in d:
        print(d[divisa])
    else:
        print("La divisa que ha introducido no está en el diccionario.")

def main():
    borrar_consola()
    d = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisa = pedir_divisa()
    comprobar_divisa(divisa, d)

if __name__ == "__main__":
    main()