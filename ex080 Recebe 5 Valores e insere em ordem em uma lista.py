'''
Crie um programa onde o usuário possa digitar cinco valores núméricos e cadastre-os em uma lista.
Já na posição correta de inserção (SEM USAR SORT())
No final, mostre a lista ordenada na tela.
Exibir onde foi adicionado o número na lista.
'''
num = []
for i in range(0, 5):
    v = ""
    while not isinstance(v, int):
        v = input("Digite um número: ")
        try:
            v = int(v)
        except ValueError:
            print("Você digitou um valor inválido, tente novamente!")
    if len(num) == 0 or v > num[-1]:
        num.append(v)
        print(f"Valor adicionado na posição {len(num)-1} da lista!")
    else:
        c = 0
        while c != len(num):
            if v <= num[c]:
                num.insert(c, v)
                print(f"Valor adicionado na posição {c} da lista!")
                break
            c += 1
print(f"Os valores digitados em ordem foram: {num}")
