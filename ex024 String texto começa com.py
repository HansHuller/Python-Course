# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO".

cidade = str(input("Digite o nome de uma cidade: ")).strip()

print("{} começa com Santo? {}".format(cidade, cidade.lower().find("santo") ==0))

if "santo" in cidade.lower().split()[0][0:5]:
    print("{} começa com SANTO!".format(cidade))
else:
    print("{} não começa com SANTO!".format(cidade))
