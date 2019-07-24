#Faça um programa que leia três números e mostre qual é o maior e o menor
cores = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
v1 = int(input("{}Digite o primeiro valor: {}".format(cores["ng"], cores["cls"])))
v2 = int(input("{}Digite o segundo valor: {}".format(cores["ng"], cores["cls"])))
v3 = int(input("{}Digite o terceiro valor: {}".format(cores["ng"], cores["cls"])))
valor = [v1, v2, v3]
menor = v1
maior = v1
if v2 < v3 and v2 < v1:
    menor = v2
if v3 < v2 and v3 < v1:
    menor = v3
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3

print("O maior dos três números é {} e menor é o {}".format(maior, menor))
print("O maior dos três números é {} e menor é o {}".format(max(valor), min(valor)))
print("O maior dos três números é {} e menor é o {}".format(sorted(valor)[-1], sorted(valor)[0]))
