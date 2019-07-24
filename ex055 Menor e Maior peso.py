'''
Faça um programa que leia o peso de cinco pessoas.
No final mostre qual foi o maior e o menor peso lidos.
'''
'''peso = []
for i in range(1, 6):
    peso.append(float(input("Digite o peso da {}ª pessoa em Kg: ".format(i))))
peso.sort()
print("O menor peso informado foi de {:.2f}Kg\nE o maior peso foi de {:.2f}Kg".format(peso[0], peso[-1]))
'''
maior = 0
menos = 0
for i in range(1, 6):
    pes = float(input("Digite o peso da {}ª pessoa em Kg: ".format(i)))
    if i == 1:
        maior = pes
        menor = pes
    else:
        if pes > maior:
            maior = pes
        if pes < menor:
            menor = pes
print("O menor peso informado foi de {:.2f}Kg\nE o maior peso foi de {:.2f}Kg".format(menor, maior))
