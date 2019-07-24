'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada número digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    num = ''
    while not isinstance(num, int):
        num = input("Qual a tabuada que deseja visualizar? ")
        try:
            num = int(num)
            break
        except ValueError:
            print("Você digitou um valor inválido, tente novamente")
    if num < 0:
        break
    print("-"*70)
    for i in range(1, 11):
        print(f"{num:^20} x {i:^20} = {num*i:>20}")
    print("-" * 70)
print("="*70)
print("Programa TABUADA finalizado, até breve!")
print("="*70)
