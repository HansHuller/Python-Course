'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor LITERAL(STR) indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
65+ voto é opcional
'''
def voto(anoDeNascimento):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - anoDeNascimento
    if idade <0:
        return "Você digitou uma Data de Nascimento inválida"
    elif idade < 16:
        return f"Com {idade} NÃO SE VOTA!"
    elif idade < 18 or idade >65:
        return f"Com {idade} É OPCIONAL VOTAR!"
    else:
        return f"Com {idade} É OBRIGATÓRIO VOTAR!"

dataNasc = int(input("Digite seu ano de nascimento: "))
print(voto(dataNasc))
