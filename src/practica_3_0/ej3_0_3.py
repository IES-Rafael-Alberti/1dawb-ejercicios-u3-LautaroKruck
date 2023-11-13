"""
Tienes este código:

    palabra = 'banana'
    contador = 0
    for letra in palabra:
        if letra == 'a':
            contador = contador + 1
    print(contador)

Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.
"""

def pedir_palabra():
    return str(input ("Introduce una palabra: "))

def contar_letra(palabra):
    cont = 0
    
    for letra in palabra:
        if letra == 'a':
            cont += 1

    return cont

def dar_cantidad(cont):
    if cont > 1:
        serie = f"La letra a aparece {cont} veces."
    elif cont == 1:
        serie = f"La letra a aparece {cont} vez."
    else:
        serie = f"La letra a no aparece ninguna vez."
    
    return serie


def main():
    palabra = pedir_palabra()
    cont = contar_letra(palabra)
    
    print(dar_cantidad(cont))


if __name__ == "__main__":
    main()

