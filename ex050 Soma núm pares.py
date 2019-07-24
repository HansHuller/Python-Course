'''
Desenvolva um programa que leia seis numeros inteiros e mostre a soma somente daqueles que forem pares.
Se o valor digitado for impar, desconsidere
'''
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
s = 0
p = 0
c = 0
for i in range(1, 7):
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        s += n
        p += 1
    c += 1
print("Você digitou {} números. Destes {} são ímpares!\n{} são pares e a soma deles é: {}".format(c, c-p, p, s))
