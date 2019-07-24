'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
expressão = list(str(input("Digite a expressão matemática que deseja validar: ")).strip().lower())
pilha = []
for i in expressão:
    if i in "(":
        pilha.append(i)
    elif i in ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append("ERRO")
            break
if len(pilha) == 0:
    print("Sua expressão é válida!")
else:
    print("Sua expressão contém um erro!")
