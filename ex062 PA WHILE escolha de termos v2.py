'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''
priterm = ''
razao = ''
ulterm = ''
c = 0
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
while not ulterm == 0:
    i = 1
    while i <= ulterm:
        print("{} → ".format(prog), end="")
        i += 1
        prog += razao
        c += 1
        if i > ulterm:
            print("PAUSA")
    ulterm = ''
    while not isinstance(ulterm, int):
        ulterm = input("Quantos termos a mais você deseja visualizar? ")
        try:
            ulterm = int(ulterm)
            break
        except ValueError:
            input("Você digitou um valor inválido, tente novamente!")
print("Progressão finalizada com {} termos exibidos!".format(c))
