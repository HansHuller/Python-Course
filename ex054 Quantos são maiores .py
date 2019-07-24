'''
Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores. (21 anos)
'''
from datetime import date
maior = 0
menor = 0
for i in range(1, 8):
    dtnasc = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(i)))
    idade = date.today().year - dtnasc
    if idade > 20:
        maior +=1
    else:
        menor +=1
print("Das sete pessoas analisadas {} delas não atingiram a maioridade e {} são maiores.".format(menor, maior))
