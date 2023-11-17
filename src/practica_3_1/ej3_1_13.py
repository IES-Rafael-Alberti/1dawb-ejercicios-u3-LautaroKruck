"""
Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
"""
from src.borrar_consola import borrar_consola

def pedir_numeros():
    try:
        numeros = input("Ingrese una muestra de números separados por comas: ")
        
        if not numeros:
            raise ValueError("No se ingresaron números.")

        return [float(numero) for numero in numeros.split(',')]

    except ValueError as e:
        print(e)
        return []

def calcular_media(lista):
    try:
        if not lista:
            return None

        media = sum(lista) / len(lista)
        return media

    except ZeroDivisionError as e:
        print(e)
        return None

def calcular_desviacion_tipica(media, lista):
    try:
        suma_cuadrados = sum((i - media) ** 2 for i in lista)

        desviacion_tipica = (suma_cuadrados / len(lista)) ** 0.5
        return desviacion_tipica

    except ZeroDivisionError as e:
        print(e)
        return None

def main():
    borrar_consola()

    lista = pedir_numeros()
    media = calcular_media(lista)

    if media is not None:
        desviacion_tipica = calcular_desviacion_tipica(media, lista)

        if desviacion_tipica is not None:
            print(f"La media de los números ingresados es: {media:.2f}")
            print(f"La desviación típica de los números ingresados es: {desviacion_tipica:.2f}")
        else:
            print("No se pudo calcular la desviación típica debido a una lista vacía.")


if __name__ == "__main__":
    main()
