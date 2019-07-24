'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''
priterm = ''
razao = ''
ulterm = ''
i = 1
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
while i <= ulterm:
    print("{} → ".format(prog), end="")
    i += 1
    prog += razao
    if i > ulterm:
        print("PAUSA")
        i = 1
        ulterm = ''
        while not isinstance(ulterm, int):
            ulterm = input("Digite quantos termos deseja visualizar: ")
            try:
                ulterm = int(ulterm)
                break
            except ValueError:
                input("Você digitou um valor inválido, tente novamente!")
    if ulterm == 0:
        i = ulterm + 1
    c += 1
print("Progressão finalizada com {} termos exibidos!".format(c))
