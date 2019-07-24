'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
expressão = list(str(input("Digite a expressão matemática que deseja validar: ")).strip().lower())
c = 0
for i in expressão:
    if i in "(":
        c += 1
    elif i in ")":
        c -= 1
    if c < 0:
        break
    print("TESTE")
if c == 0:
    print("Sua expressão é válida!")
else:
    print("Sua expressão contém um erro!")
