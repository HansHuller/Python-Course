'''
Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
lista = [[], [], []]
for i in range(1, 8):
    v = ""
    while not isinstance(v, int):
        v = input(f"Digite o {i}º valor: ")
        try:
            v = int(v)
        except ValueError:
            print("Você digitou um valor inválido, digite um nº inteiro!")
    if v % 2 == 0:
        lista[0].append(v)
        lista[1].append(v)
    else:
        lista[0].append(v)
        lista[2].append(v)
lista[0].sort()
lista[1].sort()
lista[2].sort()
print(f"Os números digitados são: {lista[0]}")
print(f"Os números pares são: {lista[1]}")
print(f"Os números ímpares são: {lista[2]}")
