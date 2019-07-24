'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
 Calcule o preço da passagem cobrando R$0,50 por KM para viagens até 200km e R$0,45 para viagens mais longas.'''

cores = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}

km = float(input("{}Qual a distância da sua viagem em kilômetros? {}".format(cores["az"], cores["cls"])))

if km > 200:
    print("{}A sua viagem de {}{}km{} custará: {}R${}{}".format(cores["rx"], cores["vm"], km, cores["rx"], cores["am"],
                                                                km*0.45, cores["cls"]))
else:
    print("{}A sua viagem de {}{}km{} custará: {}R${}{}".format(cores["rx"], cores["vm"], km, cores["rx"], cores["am"],
                                                                km * 0.50, cores["cls"]))
