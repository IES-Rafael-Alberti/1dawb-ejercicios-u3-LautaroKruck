"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""
from src.borrar_consola import borrar_consola

def pedir_fecha():
    fec_nac = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")

    dia, mes, año = fec_nac.split('/')
    dia = int(dia)
    mes = int(mes)
    año = int(año)
    try:
        if 1 <= dia <= 30: 
            return dia
        else:
            print("**Error** Día fuera de rango.")
        
        if 1 <= mes <= 12:
            return mes
        else:
            print("**Error** Mes fuera de rango.")

    except ValueError:
        print("**Error** Ingresa un número válido.")
    lista = [dia, mes, año]
    return lista

def pasar_fecha(lista):
    d = {"dia" : lista[0]}
    d = {"mes" : lista[1]}
    d = {"año" : lista[2]}

    return d

def main():
    borrar_consola()
    d = {'dia': None, 'mes': {1 : 'enero', 2 : 'febrero', 3 : 'marzo', 4 : 'abril', 5: 'mayo', 6 : 'junio', 7 : 'julio', 8 : 'agosto', 9 : 'septiembre', 10: 'octubre', 11 : 'noviembre', 12: 'diciembre'}, 'año': None,}
    lista = pedir_fecha()
    pasar_fecha(lista)

    print(f" {d['dia']} de {d['mes']} de {d['año']}")


if __name__ == "__main__":
    main()