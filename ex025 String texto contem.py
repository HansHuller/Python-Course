# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input("Digite seu nome: ")).strip()
print("{} possui SILVA? {}".format(nome, "silva" in nome.lower()))

if  "silva" in nome.lower():
    print("{} possui Silva!".format(nome))
else:
    print("{} não possui Silva! :(".format(nome))
