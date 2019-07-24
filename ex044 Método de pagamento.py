''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
 e condição de pagamento:
Se a vista dinheiro/cheque : 10% de desconto
Se a visto no cartão: 5% de desconto
Em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros'''
color = {"br": "\033[0;30m", "vm": "\033[0;31m", "vd": "\033[0;32m", "am": "\033[0;33m",
         "az": "\033[0;34m", "rx": "\033[0;35m", "cn": "\033[0;36m", "cz": "\033[0;37m",
         "cls": "\033[m", "bd": "\033[1m", "un": "\033[4m", "ng": "\033[7m"}
print("\n{:=^40}\n".format("HANSTORE"))
vprod = float(input("Digite o valor da compra: R$").replace(",", "."))
metpag = int(input("\nFormas de pagamento:"
                   "\n1 - à vista Dinheiro/Cheque"
                   "\n2 - à vista Crédito"
                   "\n3 - 2x no Crédito"
                   "\n4 - 3x ou mais crédito"
                   "\nQual opção desejada: "))
xvezes = 1
if metpag == 1:
    nvprod = vprod - (vprod * 10 / 100)
elif metpag == 2:
    nvprod = vprod * 0.95
elif metpag == 3:
    xvezes = 2
    nvprod = vprod
    print("Sua compra será parcelada em {}x de R${:.2f}".format(xvezes, nvprod / xvezes))
elif metpag == 4:
    xvezes = int(input("Em quantas vezes quer dividir o pagamento: "))
    nvprod = vprod * 1.2
    print("Sua compra será parcelada em {}x de R${:.2f}".format(xvezes, nvprod / xvezes))
else:
    print("Você selecionou um método inválido, tente novamente!")
    quit()
print("Selecionando a forma de pagamento {} sua compra de R${:.2f} terá um valor final de: R${:.2f}"
      .format(metpag, vprod, nvprod))
if nvprod < vprod:
    print("Você recebeu um desconto de: R${:.2f}".format(vprod - nvprod))
elif nvprod > vprod:
    print("Você pagará R${:.2f} de juros".format(nvprod - vprod))
