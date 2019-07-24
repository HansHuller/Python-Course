dias = int(input("Quantos dias o carro ficou alugado: "))
km = float(input("Quantos kilometros foram rodados: "))
alug = dias*60 + 0.15*km
print("O total a se pagar pelo aluguel é: R${:.2f} ".format(alug))
