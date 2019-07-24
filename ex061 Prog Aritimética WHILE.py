'''
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura WHILE.
'''
priterm = ''
razao = ''
ulterm = ''
i = 1
while not isinstance(priterm, int):
    priterm = input("Digite o primeiro termo da Progressão aritmética: ")
    try:
        priterm = int(priterm)
        break
    except ValueError:
        input("Você digitou um valor inválido, tente novamente!")
while not isinstance(razao, int):
    razao = input("Digite a razão da Progressão aritmética: ")
    try:
        razao = int(razao)
        break
    except ValueError:
        input("Você digitou um valor inválido, tente novamente!")
while not isinstance(ulterm, int):
    ulterm = input("Digite quantos termos deseja visualizar: ")
    try:
        ulterm = int(ulterm)
        break
    except ValueError:
        input("Você digitou um valor inválido, tente novamente!")
prog = priterm
while i <= ulterm:
    print("{} → ".format(prog), end="")
    i += 1
    prog += razao
print("FIM!")