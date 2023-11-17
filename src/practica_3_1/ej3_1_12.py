"""
Escribir un programa que almacene las matrices A=(123456) y B=(-100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
"""

from src.borrar_consola import borrar_consola

def multiplicar_matrices(m_a, m_b):
    resultado = []
    
    for fila in range(3):
        resultado[fila].append([])
        for columna in range(2):
            resultado[columna].append(
                m_a[fila][columna] * 
                m_b[fila][columna]
            )
    return resultado

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


def main():
    borrar_consola()

    m_a = ([1, 2], [3, 4], [5, 6])
    m_b = ([-1, 0], [0, 1], [1, 1])

    resultado = multiplicar_matrices(m_a, m_b)

    print("Matriz A:")
    mostrar_matriz(m_a)

    print("\nMatriz B:")
    mostrar_matriz(m_b)

    print("\nProducto de matrices:")
    mostrar_matriz(resultado)


if __name__ == "__main__":
    main()