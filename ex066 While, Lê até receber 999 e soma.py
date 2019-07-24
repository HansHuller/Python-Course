'''
Crie um programa que leia vários números inteiro pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando 999).
'''
cont = soma = 0
while True:
    n = ''
    while not isinstance(n, int):
        n = input("Digite um número inteiro [999 p/ parar]: ")
        try:
            n = int(n)
            break
        except ValueError:
            print("Você digitou um valor inválido, tente novamente!")
    if n == 999:
        break
    cont += 1
    soma += n
print("="*70)
print(f"Você digitou {cont} números e a soma deles é : {soma:^10}")
print("="*70)
