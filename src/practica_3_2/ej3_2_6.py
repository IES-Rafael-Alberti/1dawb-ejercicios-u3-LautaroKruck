"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
from src.borrar_consola import borrar_consola

def pedir_info():
    info = ""
    while info != "Y" and info != "N":
        info = input("¿Desea introducir información? (Y/N): ").upper()
    return info

def añadir_info(d, tipo_info):
    dato = input(f"Introduce tu {tipo_info}: ").title()
    d[tipo_info] = dato
    return d

def main():
    borrar_consola()
    diccionario_persona = {}

    info = pedir_info()

    while info == "Y":
        tipo_info = input("Introduce el tipo de información que va a introducir (por ejemplo, nombre, edad, sexo, teléfono, correo electrónico, etc.): \n").title()
        diccionario_persona = añadir_info(diccionario_persona, tipo_info)

        print(diccionario_persona)

        info = pedir_info()

if __name__ == "__main__":
    main()

