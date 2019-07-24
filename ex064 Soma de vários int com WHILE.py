'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles (Desconsiderando o flag (999))
'''
cont = 0
soma = 0
n = ''
while n != 999:
    while not isinstance(n, int):
        n = input("Insira um número inteiro [999 para parar]:")
        try:
            n = int(n)
            break
        except ValueError:
            print("Você não digitou um número inteiro. Tente novamente!")
    if n != 999:
        soma += n
        cont += 1
        n = ''
print("Você digitou {} números.\nA soma deles é: {}".format(cont, soma))
