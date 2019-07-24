'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
Quantas pessoas foram cadastradas
A média de idade do grupo.
Uma lista com todas as mulheres.
Uma lista com todas as pessoas com idade acima da média.
'''
cadastro = {}
pessoas = []
acimaMedia = mulheres = media = int()
while True:
    opcao = sexo = nome = int()
    idade = str()
    while not isinstance(nome, str):
        nome = input(f"{'Nome: ':<15}")
        try:
            nome = float(nome)
            nome = int(nome)
            print(f"Nome não pode ser um número! Tente novamente...")
        except ValueError:
            nome = str(nome)
    cadastro["nome"] = nome
    while not isinstance(sexo, str):
        sexo = input(f"{'Sexo [M/F]: ':<15}")
        try:
            sexo = float(sexo)
            sexo = int(sexo)
            print(f"Sexo não pode ser um número! Tente novamente...")
        except ValueError:
            sexo = str(sexo).upper().strip()[0]
            if sexo not in "MF":
                print("Você digitou uma opcao inválida! Tente novamente...")
                sexo = 0
    cadastro["sexo"] = sexo
    while not isinstance(idade, int):
        idade = input(f"{'Idade: ':<15}")
        try:
            idade = int(idade)
            if idade < 0:
                print(f"A idade precisa ser um valor positivo!")
        except ValueError:
            print("Idade precisa ser um número! Tente novamente...")
    cadastro["idade"] = idade
    pessoas.append(cadastro.copy())
    cadastro.clear()
    while not isinstance(opcao, str):
        opcao = input(f"{'Deseja continuar [S/N]? ':<15}")
        try:
            opcao = float(opcao)
            opcao = int(opcao)
            print(f"Não pode escolher um número! Tente novamente...")
        except ValueError:
            opcao = str(opcao).upper().strip()[0]
            if opcao not in "SN":
                print("Você digitou uma opcao inválida! Tente novamente...")
                opcao = 0
    if opcao == "N":
        break
for i in pessoas:
    media += i["idade"]
    if i["sexo"] == "F":
        mulheres += 1
media = media/len(pessoas)
for i in pessoas:
    if i["idade"] > media:
        acimaMedia += 1
print("=-="*23)
print(f"A) Foram cadastradas {len(pessoas)} pessoas.")
print(f"B) A média de idade é de {media:.2f} anos.")
if mulheres > 0:
    for c, i in enumerate(pessoas):
        if c == 0:
            print(f"C) As mulheres cadastradas foram: ", end="")
        if i["sexo"] == "F":
            print(f"{i['nome']} - ", end="")
        if c == len(pessoas)-1:
            print()
else:
    print("C) Não foram cadastradas mulheres.")
if acimaMedia > 0:
    for c, i in enumerate(pessoas):
        if c == 0:
            print(f"D) Lista das pessoas que estão com idade acima da média:")
        if i["idade"] > media:
            print("    ", end="")
            for k, v in i.items():
                print(f"{k.capitalize()} = {v:^10}|| ", end="")
            print()
else:
    print(f"D) Todos estão na média!")
