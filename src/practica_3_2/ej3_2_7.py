"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
"""
from src.borrar_consola import borrar_consola

def pedir_info():
    info = ""
    while info != "Y" and info != "N":
        info = input("¿Desea introducir más artículos? (Y/N): ").upper()
    return info

def añadir_articulo(lista_de_compra, artículo):
    precio = input(f"Introduce el precio de {artículo}: ").title()
    lista_de_compra[artículo] = float(precio)
    return lista_de_compra

def calcular_total(lista_de_compra):
    total = sum(lista_de_compra.values())

    lista_de_compra.setdefault('Total', total )

def main():
    borrar_consola()
    lista_de_compra = {}

    info = pedir_info()

    while info == "Y":
        artículo = input("Introduce el artículo: \n").title()
        lista_de_compra = añadir_articulo(lista_de_compra, artículo)

        print(lista_de_compra)

        info = pedir_info()

    calcular_total(lista_de_compra)
    print(lista_de_compra)



if __name__ == "__main__":
    main()

