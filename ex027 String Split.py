# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite seu nome: ")).strip().split()

print("Seu primeiro nome é: {}\nSeu último nome é: {}".format(nome[0], nome[-1]))
print("Seu primeiro nome é: {}\nSeu último nome é: {}".format(nome[0], nome[len(nome)-1]))
