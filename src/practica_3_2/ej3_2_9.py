"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""
from src.borrar_consola import borrar_consola


def mostrar_menu():
    print("\nMenú:")
    print("1. Añadir una nueva factura")
    print("2. Pagar una factura existente")
    print("3. Terminar")


def añadir_factura(base_datos):
    num_factura = input("Ingrese el número de factura: ")

    while not num_factura.isnumeric():
        print("**ERROR** Número de factura no válido.")
        num_factura = input("Ingrese el número de factura: ")

    coste_factura = input("Ingrese el coste de la factura: ")

    while not coste_factura.isnumeric():
        print("**ERROR** Coste no válido.")
        coste_factura = input("Ingrese el coste de la factura: ")

    base_datos[num_factura] = float(coste_factura)
    print(f"Factura con clave {num_factura} añadida correctamente.")


def pagar_factura(base_datos, facturas_pagadas):
    num_factura = input("Ingrese el número de factura que desea pagar: ")

    try:
        coste_factura = base_datos.pop(num_factura)
        print(f"Factura con clave {num_factura} pagada correctamente. Coste: {coste_factura}")
        facturas_pagadas[num_factura] = coste_factura
    except KeyError:
        print(f"No se encontró una factura con clave {num_factura} en la base de datos.")


def calcular_pendiente(base_datos):
    return sum(base_datos.values())


def calcular_pagado(facturas_pagadas):
    return sum(facturas_pagadas.values())


def main():
    borrar_consola()

    base_datos_facturas = {}
    facturas_pagadas = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            añadir_factura(base_datos_facturas)
        elif opcion == '2':
            pagar_factura(base_datos_facturas, facturas_pagadas)
        elif opcion == '3':
            print("Programa terminado.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 3.")

        pendiente = calcular_pendiente(base_datos_facturas)
        pagado = calcular_pagado(facturas_pagadas)

        print(f"Cantidad pendiente de cobro: {pendiente}")
        print(f"Cantidad cobrada hasta el momento: {pagado}")


if __name__ == "__main__":
    main()

