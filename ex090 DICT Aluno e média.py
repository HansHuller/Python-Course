'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela. (>=7 aprovado <7 reprovado)
'''
aluno = dict()
média = " "
nome = 0
while not isinstance(nome, str):
    nome = input("Nome do aluno: ")
    try:
        nome = float(nome)
        nome = int(nome)
        print("Nome não pode ser um número, tente novamente.")
    except ValueError:
        nome = str(nome)
while not isinstance(média, float):
    média = input(f"Média do {nome}: ")
    try:
        média = float(média)
        if média > 10:
            print("Você digitou um valor inválido, tente novamente.")
            média = " "
    except ValueError:
        print("Você digitou um valor inválido, tente novamente.")
aluno["nome"] = nome
aluno["média"] = média
if aluno["média"] >= 7:
    aluno["situação"] = "aprovado"
elif aluno["média"] >= 5:
    aluno["situação"] = "recuperação"
else:
    aluno["situação"] = "reprovado"

for k, v in aluno.items():
    print(f"{k.capitalize():<10}: {v}")
