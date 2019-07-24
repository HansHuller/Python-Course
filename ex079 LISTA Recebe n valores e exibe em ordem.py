'''
Digite um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
num = []
while True:
    v = ""
    r = "erro"
    while not isinstance(v, int):
        v = input("Digite um valor: ")
        try:
            v = int(v)
        except ValueError:
            print("Você digitou um valor inválido, tente novamente!")
    if v in num:
        print("Este valor já foi digitado! Ele será descartado!")
    else:
        num.append(v)
        print("Este valor foi adicionado com sucesso!")
    while r not in "SN":
        r = input("Voce deseja digitar outro valor [S/N]? ").upper().strip()[0]
        if r not in "SN":
            print("Você digitou um valor inválido, tente novamente!")
    if r == "N":
        break
num.sort()
print("Você digitou os valores: ", end="")
for i in num:
    print(f"{i}  ", end="")
