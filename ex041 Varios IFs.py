''' A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 = MIRIM
ATÉ 14 = INFANTIL
ATÉ 19 = JUNIOR
ATÉ 25 = SÊNIOR
MAIOR DE 25 = MASTER'''
from datetime import date
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
idade = date.today().year - int(input("Digite sua data de Nascimento: "))
if idade <= 9:
    print("Com {} anos você se enquadra na categoria MIRIM!".format(idade))
elif idade <= 14:
    print("Com {} anos você se enquadra na categoria INFANTIL!".format(idade))
elif idade <= 19:
    print("Com {} anos você se enquadra na categoria JÚNIOR!".format(idade))
elif idade <= 25:
    print("Com {} anos você se enquadra na categoria SÊNIOR!".format(idade))
else:
    print("Com {} anos você se enquadra na categoria MASTER!".format(idade))
