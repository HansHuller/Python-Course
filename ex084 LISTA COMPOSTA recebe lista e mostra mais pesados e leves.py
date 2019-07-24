'''
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
Quantas pessoas foram cadastradas
Uma listagem com as pessoas mais pesadas (mais pesado e mais leve são definidos de acordo com dados recebidos)
Uma listagem com as pessoas mais leves
'''
lpessoas = []
pessoa = []
maiorp = menorp = c = 0
lispesados = []
lisleve = []
while True:
    test = "erro"
    v = 0
    pessoa.clear()
    while not isinstance(v, str):
        v = input("Digite o Nome: ")
        try:
            v = float(v)
            v = int(v)
            print("Nome não pode ser um número, tente novamente.")
        except ValueError:
            v = str(v)
    pessoa.append(v)
    while not isinstance(v, float):
        v = input("Digite o Peso: ")
        try:
            v = float(v)
        except ValueError:
            print("Você digitou um peso inválido, tente novamente.")
    pessoa.append(v)
    lpessoas.append(pessoa[:])
    if c != 0:
        if v > lpessoas[maiorp][1]:
            maiorp = c
        if v < lpessoas[menorp][1]:
            menorp = c
    while test not in "SN":
        test = input("Deseja continuar [S/N]?  ").strip().upper()[0]
    if test in 'N':
        break
    c += 1
for i in lpessoas:
    if i[1] == lpessoas[maiorp][1]:
        lispesados.append(i[0])
    if i[1] == lpessoas[menorp][1]:
        lisleve.append(i[0])
print("=-"*35)
print(f"Você realizou {len(lpessoas)} novos cadastros.")
print(f"As pessoas pesadas são {lispesados} e elas pesam {lpessoas[maiorp][1]}Kg")
print(f"O menor peso foi {lpessoas[menorp][1]}Kg. O peso de: ", end="")
for i in lpessoas:
    if i[1] == lpessoas[menorp][1]:
        print(f" [{i[0]}] ", end="")
print()
print("=-"*35)
