'''
Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
num = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze",
       "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    n = select = ' '
    while not isinstance(n, int):
        n = input("Selecione um número entre 0 e 20: ")
        try:
            n = int(n)
            if not (0 <= n <= 20):
                n = ''
                print("Você digitou um valor inválido, tente novamente.")
        except ValueError:
            print("Você digitou um valor inválido, tente novamente.")
    print(f"Você selecionou o número {num[n]}")
    while True:
        select = str(input("Você deseja continuar [S/N]: ")).strip().upper()
        if select != "S" and select != "N":
            print("Você digitou um valor inválido, tente novamente.")
        else:
            break
    if select == "N":
        break
