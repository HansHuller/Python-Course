'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''
lis = []
par = []
impar = []
while True:
    v = ""
    r = " "
    while not isinstance(v, int):
        v = input("Digite um número: ")
        try:
            v = int(v)
        except ValueError:
            print("Você digitou um valor inválido, tente novamente!")
    lis.append(v)
    while r not in "SN":
        r = input("Deseja continuar [S/N]?  ").strip().upper()[0]
        if r not in "SN":
            print("Você selecionou uma opção inválida, tente novamente!")
    if r in "N":
        break
for i in lis:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print("-=-"*23)
print(f"A lista digitada é: {lis}")
if len(par) > 1:
    print(f"Os números pares digitados foram: {par}")
elif len(par) == 1:
    print(f"O número par digitado foi: {par}")
else:
    print("Não foram digitados números pares.")
if len(impar) > 1:
    print(f"Os números ímpares digitados foram: {impar}")
elif len(impar) == 1:
    print(f"O número ímpar digitado foi: {impar}")
else:
    print("Não foram digitados números pares.")