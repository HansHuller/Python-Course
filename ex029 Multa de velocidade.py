# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velat = float(input("Qual a velocidade atual do carro: "))

if velat > 80:
    print("Tá com pressa boneco?\nSua ansiedade te gerou uma multa de: R${:.2f}\nTá felizinho? Valeu a pena?".format((velat-80)*7))
print("Dirija com segurança e tenha um bom dia!")
