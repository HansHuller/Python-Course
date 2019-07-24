'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualqer como parâmetro e mostre
uma mensagem com tamanho adaptável. (linha = tamanho da frase)
'''
def escreva(frase):
    frase = "  " + frase + "  "
    tam = len(frase)
    print("-" * tam)
    print(f"{frase.upper()}")
    print("-" * tam)


#Inicio do programa
escreva(str(input("Digite o título desejado: ")))