'''
Aprimore o desafio anterior, mostrando no final:
A soma de todos os valores pares digitados.
A soma dos valores da terceira coluna.
O maior valor da segunda linha.
'''
matriz = [[], [], []]
somater = parsom = maior = 0
for i in range(0, 9):
    v = ""
    while not isinstance(v, int):
        v = input(f"Digite o valor do endereço [{int(i/len(matriz))},{i % len(matriz)}]: ")
        try:
            v = int(v)
        except ValueError:
            print("Você digitou um valor inválido, digite um nº inteiro!")
    matriz[i % len(matriz)].append(v)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[c][l]:^5}]", end="")
        if matriz[c][l] % 2 == 0:
            parsom += matriz[c][l]
        if c == 2:
            somater += matriz[c][l]
        if l == 1:
            if c == 0:
                maior = matriz[c][l]
            elif matriz[c][l] > maior:
                maior = matriz[c][l]
    print()
print("-=-"*30)
'''for l in range(0, len(matriz)):
    for c in range(0, len(matriz)):
        if matriz[c][l] % 2 == 0:
            parsom += matriz[c][l]
for l in range(0, len(matriz)):
    col = 2
    somater += matriz[col][l]
for c in range(0, len(matriz)):
    lin = 1
    if c == 0:
        maior = matriz[c][lin]
    elif matriz[c][lin] > maior:
        maior = matriz[c][lin]'''
print(f"A soma dos valores pares é igual a: {parsom}")
print(f"A soma dos valores da terceira coluna é: {somater}")
print(f"O maior número da segunda linha é: {maior}")
