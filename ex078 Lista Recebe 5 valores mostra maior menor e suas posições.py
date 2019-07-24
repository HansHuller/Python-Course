'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
IMPORTANTE>>>: Leva em consideração se a lista repetir os menores e maiores valores.
'''
lista = []
for i in range(1, 5+1):
    v = ''
    while not isinstance(v, int):
        v = input(f"Digite o valor da {i}ª posição: ")
        try:
            v = int(v)
        except ValueError:
            print("Você digitou um valor inválido, tente novamente!")
    lista.append(v)
print(f"Você digitou os valores: ", end="")
for val in lista:
    print(f"{val}  ", end="")
print()
maior = max(lista)
menor = min(lista)
posmaior = []
posmenor = []
for c, v in enumerate(lista):
    if v == maior:
        posmaior.append(c+1)
    if v == menor:
        posmenor.append(c+1)
print("-="*35)
if len(posmaior) > 1:
    print(f"O maior valor digitado foi {maior} e ele apareceu nas posições: ", end="")
    for v in posmaior:
        print(f"{v}  ", end="")
    print()
else:
    print(f"O maior valor digitado foi {maior} e ele apareceu na posição: {posmaior[0]}")
if len(posmenor) > 1:
    print(f"O menor valor digitado foi {menor} e ele apareceu nas posições: ", end="")
    for v in posmenor:
        print(f"{v}  ",end="")
    print()
else:
    print(f"O menor valor digitado foi {menor} e ele apareceu na posição: {posmenor[0]}")
