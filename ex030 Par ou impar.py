# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
cores = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
num = int(input("{}Digite um número inteiro: {}".format(cores["rx"], cores["cls"])))
print("{}-=-{}".format(cores["am"], cores["cls"])*18)
if num % 2:
    print("O seu número {}{}{}, é {}impar{}!".format(cores["vm"], num, cores["cls"], cores["bd"], cores["cls"]))
else:
    print("O seu número {}{}{}, é {}par{}!".format(cores["vm"], num, cores["cls"], cores["bd"], cores["cls"]))
