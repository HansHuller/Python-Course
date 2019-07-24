'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela com a formatação correta.
[  1  ][  1  ][  1  ]
[  1  ][  1  ][  1  ]
[  1  ][  1  ][  1  ]
'''
matriz = [[], [], []]
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
    print()
