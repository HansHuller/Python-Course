# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao to do sem considerar espaços
# Quantas letras tem o primeiro nome

nome = str(input("Digite seu nome: ")).strip()

print("Seu nome com todas as letras maiúsculas é: {}".format(nome.upper()))
print("Seu nome com todas as letras minúsculas é: {}".format(nome.lower()))
print("Seu nome possui um total de {} caractéres!".format(len(nome.replace(" ",""))))
print("Seu nome possui um total de {} caractéres!".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome é {} e possui {} caractéres!".format(nome.split()[0], len(nome.split()[0])))
