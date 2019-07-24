# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
from datetime import date
cores = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}

ano = int(input("{}Digite o ano que deseja sabe se é bissexto:\nDigite 0 pro ano atual!!! {}".format(cores["vm"], cores["cls"])))
if ano == 0:
    ano = date.today().year
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0 ):
    print("{}{}{} é um ano {}Bissexto!!{}".format(cores["rx"], ano, cores["cls"], cores["vd"], cores["cls"]))
else:
    print("{}{}{} {}não é{} um ano Bissexto!!".format(cores["rx"], ano, cores["cls"], cores["bd"], cores["cls"]))
