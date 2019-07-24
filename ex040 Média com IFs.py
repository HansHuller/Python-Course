''' Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com sua média:
Média abaixo de 5 = Reprovado
Média entre 5 e 6.9 = Recuperação
Média 7 ou maior = Aprovado
Tentar fazer com várias notas
'''
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1+n2)/2
if media <5:
    print("Sinto em lhe informar que vossa senhoria está {}REPROVADO!!!{}\n"
          "Sua média foi {:.2f}... Faltaram {:.2f} pontos para você ficar de recuperação e "
          "{:.2f} pontos para você conseguir ser aprovado... :(".format(color["vm"], color["cls"], media, 5-media,
                                                                        7-media))
elif media < 7:
    print("Você ainda tem chances! Vossa senhoria está de {}RECUPERAÇÃO!{}.\n"
          "Sua média foi {:.2f}... Faltaram {:.2f} pontos para você ser aprovado... :@"
          .format(color["am"], color["cls"], media, 7 - media))
elif media == 10:
    print("Você está de parabéns! Vossa senhoria está {}APROVADA COM A NOTA MÁXIMA DE {:.2f}!!!!!!!!{}.\n"
          .format(color["vd"], media, color["cls"]))
else:
    print("Você está de parabéns! Vossa senhoria está {}APROVADA!{}.\n"
          "Sua média foi {:.2f} :) faltaram somente {:.2f} pontos para alcançar o 10... :)"
          .format(color["vd"], color["cls"], media, 10 - media))
