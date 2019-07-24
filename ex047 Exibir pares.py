'''
Cria um programa que mostre na tela todos os números pares entre 1 e 50
'''
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print("\nAcabou!")

for i in range(2, 51, 2):
    print(i, end=" ")
print("\nAcabou!")
