'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (inteiro) e o programa vai informar
quantas cédulas de cada valor serão entregues.
OBS. Considere que o caixa possui cédulas de 50, 20, 10 e 1.
'''
saque = ''
céd = 50
totcéd = 0
print("="*70)
print("{:^70}".format("BANCO HH"))
print("="*70)
while not isinstance(saque, int):
    saque = input("Quanto deseja sacar? R$")
    try:
        saque = int(saque)
        if saque < 0:
            print("Você digitou um valor inválido, tente novamente")
            saque = ""
        break
    except ValueError:
        print("Você digitou um valor inválido, tente novamente")
total = saque
while True:
    if total >= céd:
        totcéd = total // céd
        total = total % céd
        print(f"Você receberá {totcéd} notas de R${céd}.00")
    else:
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
    if total == 0:
        break
print("="*70)
print("{:^70}".format("Obrigado e volte sempre!"))