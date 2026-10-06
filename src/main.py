import numpy as np

def main():
    # Definição das matrizes 2x2
    A = np.array([
        [1, 2],
        [3, 4]
    ])

    B = np.array([
        [5, 6],
        [7, 8]
    ])

    # Soma das matrizes
    C = A + B

    # Exibição no console
    print("Matriz A:")
    print(A)

    print("\nMatriz B:")
    print(B)

    print("\nA + B:")
    print(C)


if __name__ == "__main__":
    main()