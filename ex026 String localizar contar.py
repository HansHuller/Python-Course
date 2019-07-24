# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece pela última vez

frase = str(input("Digite um texto: ")).strip()
print("A letra {}A{} se repete {} vezes na sua frase!".format(chr(34), chr(34), frase.lower().count("a")))
print("A letra {}A{} aparece pela primeira vez no endereço: {}".format(chr(34), chr(34), frase.lower().find("a")))
print("A letra {}A{} aparece pela última vez no endereço: {}".format(chr(34), chr(34), frase.lower().rfind("a")))
