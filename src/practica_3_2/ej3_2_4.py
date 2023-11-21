from src.borrar_consola import borrar_consola

def pedir_fecha():
    fec_nac = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")

    dia, mes, año = map(int, fec_nac.split('/'))

    if 1 <= dia <= 31 and 1 <= mes <= 12:
        return dia, mes, año
    else:
        print("**Error** Día o mes fuera de rango.")
        return None

def pasar_fecha(lista):
    d = {'dia': lista[0], 'mes': lista[1], 'año': lista[2]}
    return d

def main():
    borrar_consola()
    meses = {1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'}
    
    fecha = pedir_fecha()

    if fecha:
        d = pasar_fecha(fecha)
        print(f"{d['dia']} de {meses[d['mes']]} de {d['año']}")

if __name__ == "__main__":
    main()
