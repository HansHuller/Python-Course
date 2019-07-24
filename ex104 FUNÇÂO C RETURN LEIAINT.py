'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
'''


def inputInt(frase = "Digite um número inteiro: ", nomeVar = "Variável"):
    aux = " "
    while not isinstance(aux, int):
        aux = input(f"{frase:<30}")
        try:
            aux = int(aux)
        except ValueError:
            print(f"\033[1;31m{nomeVar.upper()}\033[m \033[0;31mprecisa ser um número inteiro! Tente novamente...\033[m")
    return aux


# Programa Principal
num = inputInt("Digite sua idade: ", "Idade")
print(f"Sua idade é {num}!")
