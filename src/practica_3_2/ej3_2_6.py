"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
from src.borrar_consola import borrar_consola

def pedir_info():

    info = ""
    while info != "Y" and info != "N":
        info = input("Desea introducir información (Y/N): ").upper()

    return info

def añadir_info(d, msj1, msj2):
    
    d.setdefault(input(msj1).title(), input(msj2).title())

    return d

def main():
    borrar_consola()
    d = dict()

    msj1 = "Introduzca el tipo de informacion que va a introducir (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.): \n"
    msj2 = "Introduzca el dato: \n"

    info = pedir_info()

    while  info == "Y" :
        añadir_info(d, msj1, msj2)
        print(d)

        info = pedir_info()


if __name__ == "__main__":
    main()