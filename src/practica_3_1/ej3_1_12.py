"""
Escribir un programa que almacene las matrices A=(123456) y B=(-100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
"""

from src.borrar_consola import borrar_consola

def multiplicar_matrices(matriz_a, matriz_b):
    if len(matriz_a[0]) != len(matriz_b):
        raise ValueError("No se pueden multiplicar las matrices. El número de columnas de A debe ser igual al número de filas de B.")

    resultado = [[0 for _ in range(len(matriz_b[0]))] for _ in range(len(matriz_a))]
    
    for i in range(len(matriz_a)):
        for j in range(len(matriz_b[0])):
            for k in range(len(matriz_b)):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return resultado

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


def main():
    borrar_consola()

    matriz_a = [[1, 2, 3], [4, 5, 6]]
    matriz_b = [[-1, 0, 0], [1, 1, 1]]

    producto = multiplicar_matrices(matriz_a, matriz_b)

    print("Matriz A:")
    mostrar_matriz(matriz_a)

    print("\nMatriz B:")
    mostrar_matriz(matriz_b)

    print("\nProducto de matrices:")
    mostrar_matriz(producto)


if __name__ == "__main__":
    main()