"""

Escribir un programa que preprnte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
from src.borrar_consola import borrar_consola

def pedir_nombre(d):
    nom = input("Introduce tu nombre: ")
    d["nombre"] = nom.title()

def pedir_edad(d):
    edad_valida = False
    while not edad_valida:
        age = input("Introduce tu edad: ")
        if age.isnumeric() and 1 <= int(age) <= 120:
            d["edad"] = age
            edad_valida = True
        else:
            print("Por favor, introduce una edad válida (número entero entre 1 y 120).")

def pedir_direccion(d):
    direc = input("Introduce tu dirección: ")
    d["dirección"] = direc.title()

def pedir_telefono(d):
    telefono_valido = False
    while not telefono_valido:
        tel = input("Introduce tu número de teléfono: ")
        if tel.isnumeric() and len(tel) == 10: 
            d["teléfono"] = tel
            telefono_valido = True
        else:
            print("Por favor, introduce un número de teléfono válido (10 dígitos).")

def main():
    borrar_consola()

    d = {"nombre": None, "edad": None, "dirección": None, "teléfono": None}
    
    pedir_nombre(d)
    pedir_edad(d)
    pedir_direccion(d)
    pedir_telefono(d)

    print(f"{d['nombre']} tiene {d['edad']} años, vive en {d['dirección']} y su número de teléfono es {d['teléfono']}")

if __name__ == "__main__":
    main()