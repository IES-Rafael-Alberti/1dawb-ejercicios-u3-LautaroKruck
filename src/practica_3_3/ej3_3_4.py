"""
Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

1. Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
2. Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
3. Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
4. Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.
"""
from src.borrar_consola import borrar_consola


def main():
    borrar_consola()

    frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}

    frutas_unicas =  frutas1 | frutas2
    print("Nombres no repetidos => ", frutas_unicas)

    frutas_comunes =    frutas1 & frutas2
    print("Nombres que se repiten => ", frutas_comunes)
    
    frutas_solo_en_frutas1 = frutas1 - frutas2
    print("Frutas que están en frutas1 pero no en frutas2 => ", frutas_solo_en_frutas1)  
    
    frutas_solo_en_frutas2 = frutas2 - frutas1
    print("Frutas que están en frutas2 pero no en frutas1 => ", frutas_solo_en_frutas2)


if __name__ == "__main__":
    main()