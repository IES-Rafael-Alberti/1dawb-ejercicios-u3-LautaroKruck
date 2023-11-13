"""
Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.
"""
def pedir_palabra():
    return str(input ("Introduce una palabra: "))

def palabra_al_reves(palabra):
    indice = 0
    serie = ""
    while indice < len(palabra):
        serie += f"\n {palabra[indice]} \n"
        indice += 1
    return serie

def main():
    palabra = pedir_palabra()
    serie = palabra_al_reves(palabra)
    print(serie)

if __name__ == "__main__":
    main()