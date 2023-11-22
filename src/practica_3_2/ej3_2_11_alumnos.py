"""
Ejercicio 3.2.11
El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica. Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos con la información contenida en el directorio.

"nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información del cliente. Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como valores la información de cada cliente correspondientes a los campos. Es decir, un diccionario como el siguiente

{'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}
"""


def main():
    directorio_texto = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

    # Dividir la cadena de texto en líneas
    lineas = directorio_texto.split('\n')

    # Inicializar el diccionario
    directorio_clientes = {}

    # Procesar cada línea (excepto la primera que contiene los nombres de los campos)
    for linea in lineas[1:]:
        # Solo tratar líneas con contenido e ignorar líneas vacías...
        if linea:
            # Dividir la línea en valores usando el punto y coma como separador
            valores = linea.split(';')

            # Obtener el nif del cliente (primer valor en la línea)
            nif = valores[0]

            # Crear un diccionario con la información del cliente
            cliente_info = {
                "nombre": valores[1],
                "email": valores[2],
                "teléfono": valores[3],
                "descuento": float(valores[4])  # Convertir el descuento a float
            }

            # Añadir el diccionario del cliente al diccionario directorio_clientes
            directorio_clientes[nif] = cliente_info

    # Mostrar el diccionario resultante
    print(directorio_clientes)

if __name__ == "__main__":
    main()


