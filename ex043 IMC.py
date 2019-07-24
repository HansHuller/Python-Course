''' Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:
< 18.5 = abaixo do peso
< 25   = peso ideal
< 30   = sobrepeso
< 40   = Obesidade
>= 40   = Obesidade mórbida'''
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
peso = float(input("Olá! Por favor, informe seu peso em KG: ").replace(",", "."))
altura = float(input("Por favor, informe sua altura em metros: ").replace(",", "."))
imc = peso / (altura ** 2)
print("-=-"*18, "\nCom {:.2f}m de altura e pesando {:.2f}Kg, seu IMC é: {:.2f}\nOu seja, você ".format(altura, peso,imc), end="")
if imc < 18.5:
    print("está ABAIXO DO PESO!")
elif imc < 25:
    print("está com o PESO IDEAL!!")
elif imc < 30:
    print("está com SOBREPESO!!")
elif imc < 40:
    print("está OBESO!!")
else:
    print("tem OBESIDADE MÓRBIDA, você é o {}ZAFÃO!!! Seu peso pode ser medido em ARROBAS!!!".format(color["vm"]))
