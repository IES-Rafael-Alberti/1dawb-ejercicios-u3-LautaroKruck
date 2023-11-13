"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

def pedir_num():
    while error:
        try:
            num = int(input(""))
        
        except:

        except:
            

    if num <= 0 or num >= 50:
        raise Exception("**Error** Número introducido no válido") 
    
    return num

def pedir_reintegro():
    reintegro = int(input("Ingresa el reintegro: "))

    if reintegro <= 0 or reintegro >= 10:
        raise Exception("**Error** Número introducido no válido") 
    return reintegro

def guardar_num(num):
    lista = []
    cont = 1
    for i in range (6):
        print (f"Número {cont}: {num}")
        cont += 1
        lista.append(input)
    return lista

def tupla_loteria(lista, reintegro):
    loteria = (lista, reintegro)
    return loteria

def dar_lista(lista_num):
    serie = ""
    print("Los números ganadores de la lotería primitiva son: \n")
    cont = 1
    for num in lista_num:

        serie += f"\n {num:.0f} \n"
    return serie

def main():
    print("Introduzca los números de la lotería: \n")
    num = pedir_num()
    reintegro = pedir_reintegro()
    lista = guardar_num(num)
    loteria = tupla_loteria(lista, reintegro)


if __name__ == "__main__":
    main()