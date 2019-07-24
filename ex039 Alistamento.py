''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar no serviço militar
Se é a hora de se alistar
Se já passou da hora de se alistar
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
sexo = str(input("Bom dia! Por favor informe seu sexo (M = Masculino / F = Feminino): ")).upper()
if sexo != "F" and sexo != "M":
    print("Você não digitou um sexo válido! Tente novamente!")
elif sexo == "F":
    print("Saudações, dama! Você não precisa se alistar!")
else:
    ano = int(input("{}Bom dia, jovem! Você está curioso sobre seu alistamento no {}serviço militar?{}\n"
                "{}Para saber mais digite seu ano de nascimento: {}".format(color["az"], color["vm"], color["cls"],
                                                                            color["vd"],color["cls"])))
    idade = date.today().year - ano
    print("Você que nasceu em {} completa neste ano {} anos!\nO momento ideal para seu alistamento seria em {}\n"
          "Portanto:".format(ano, idade, ano+18))
    print("\033[7m-=-\033[m"*18)
    if idade < 18:
        print("{}Fique tranquilo! Você ainda NÃO PRECISA se alistar!! Ainda falta {} ano(s)!{}".format(color["vd"], 18-idade
                                                                                                       , color["cls"]))
    elif idade == 18:
        print("{}Fique atento, Champs! JÁ ESTÁ NA HORA DE SE ALISTAR!!{}".format(color["am"], color["cls"]))
    else:
        print("{}TÁ MOSCANDO, PARÇA! Você já deveria ter se alistado há {} ano(s)!!!!{}".format(color["vm"], idade - 18
                                                                                                , color["cls"]))
