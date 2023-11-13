"""
Hay un método de cadenas llamado count que es similar a find. Lee la documentación de este método en: * Métodos en ingles * Métodos en castellano
y escribe el código necesario para invocar a este método y contar el número de veces que una letra aparece en “banana”.
"""

def pedir_palabra():
    return str(input ("Introduce una palabra: "))

def pedir_letra():
    return str(input ("Introduce una letra: "))

def contar_letra(palabra , let):
    cont = 0
    
    for letra in palabra:
        if letra == let:
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
    let = pedir_letra()
    cont = contar_letra(palabra , let)
    
    print(dar_cantidad(cont))


if __name__ == "__main__":
    main()