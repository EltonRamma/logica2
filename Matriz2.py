cinema = [[0 for _ in range(8)] for _ in range(5)]

matriz = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40]
]

def reserva_assento(cinema, linha, coluna):
    posicao_l = linha-1
    posicao_c = coluna-1
    if 0 <= posicao_l < 5 and 0 <= posicao_c < 8:
        if cinema[posicao_l][posicao_c] == 0:
            cinema[posicao_l][posicao_c] = 1
            print(f"\nA cadeira [{linha}][{coluna}] foi reservada.")
        else:
            print(f"\nA cadeira [{linha}][{coluna}] já está reservada.")
    else:
        print("\nPosição inválida. Escolha uma linha entre 0-4 e uma coluna entre 0-7.")

def exibir(cinema, dim_linha, dim_coluna):
    for i in range(dim_linha):
        for j in range(dim_coluna):
            print(cinema[i][j], end=' ')
        print()

exibir(cinema, 5, 8)
reserva_assento(cinema, 2, 5)
exibir(cinema, 5, 8)
