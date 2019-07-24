'''
Crie um programa que leia, nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
em um dicionário, se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
Aposenta depois de 35 anos de contribuição.
'''
pessoa = {}
from datetime import date
while True:
    aux = 0
    while not isinstance(aux, str):
        aux = input(f"{'NOME: ':<30}")
        try:
            aux = float(aux)
            aux = int(aux)
            print(f"Nome não pode ser um número! Tente novamente...")
        except ValueError:
            aux = str(aux)
    pessoa["nome"] = aux
    while not isinstance(aux, int):
        aux = input(f"{'ANO DE NASCIMENTO: ':<30}")
        try:
            aux = int(aux)
            if aux >= (date.today().year - 18):
                aux = " "
                print(f"Ano de Nascimento precisa ser menor {date.today().year - 18}")
        except ValueError:
            print("Ano precisa ser um número inteiro! Tente novamente...")
    pessoa["idade"] = date.today().year - aux
    anoNasc = aux
    aux = " "
    while not isinstance(aux, int):
        aux = input(f"{'CTPS (0 caso não tenha): ':<30}")
        try:
            aux = int(aux)
        except ValueError:
            print("CTPS precisa conter números! Tente novamente...")
    pessoa["CTPS"] = aux
    if pessoa["CTPS"] == 0:
        for k, v in pessoa.items():
            print(f"{k} é {v}")
        break
    aux = " "
    while not isinstance(aux, int):
        aux = input(f"{'ANO DE CONTRATAÇÃO: ':<30}")
        try:
            aux = int(aux)
            if aux < (anoNasc + 18):
                aux = " "
                print(f"O trabalho com carteira assinada só é possível após os 18 anos, tente novamente.")
        except ValueError:
            print("Ano precisa ser um número inteiro! Tente novamente...")
    pessoa["ano de contratação"] = aux
    aux = " "
    while not isinstance(aux, float):
        aux = input(f"{'SALÁRIO: ':<30}")
        try:
            aux = float(aux)
        except ValueError:
            print("Salário precisa ser um número! Tente novamente...")
    pessoa["salário"] = aux
    pessoa["aposentadoria"] = pessoa["idade"] - (date.today().year - pessoa["ano de contratação"]) + 35
    for k, v in pessoa.items():
        print(f"{k.capitalize():<20} = {v}")
    break
