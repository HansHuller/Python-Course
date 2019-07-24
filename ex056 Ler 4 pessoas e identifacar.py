'''
Desenvolva um programa que leia o nome idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do Grupo
Qual é o nome do homem mais velho
Quantas mulheres têm menos de 20 anos.
'''
mulheresmenores = 0
idade = []
homens = 0
nomehomemvelho = ''
idadedohomemvelho = 0
for i in range(0, 4):
    print("-------- {}ª PESSOA --------".format(i+1))
    nome = str(input("Nome: ".format(i+1)))
    idade.append(int(input("Idade: ")))
    sexo = str(input("Sexo [f/m]: ")).upper()
    if sexo == "F" and idade[i] < 20:
        mulheresmenores += 1
    if sexo == "M" and idade[i] > idadedohomemvelho:
        idadedohomemvelho = idade[i]
        nomehomemvelho = nome
        homens += 1
print("A média de idade do grupo é de {:.0f} anos".format(sum(idade)/len(idade)))
if mulheresmenores == 0:
    print("Não haviam mulheres menores no grupo.")
else:
    print("Ao todo o grupo possui {} mulheres menores de 20 anos".format(mulheresmenores))
if homens > 0:
    print("O homem mais velho tem {} anso e se chama {}".format(idadedohomemvelho, nomehomemvelho))
else:
    print("Não haviam homens no grupo.")


'''for i in range(0, 4):
    nome.append(str(input("\nDigite o nome da {}ª pessoa: ".format(i+1))))
    idade.append(int(input("Quantos anos ela tem? ")))
    sexo.append(str(input("Qual o sexo dela? ".format(i+1))))
print("A média de idade do grupo é de {:.0f} anos".format(sum(idade)/len(idade)))'''