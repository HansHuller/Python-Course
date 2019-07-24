'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
Qual é o total gasto na compra.
Quantos produtos custam mais de R$1.000
Qual é o nome do produto mais barato.
'''
qntd = total = prodcaro = maisbaratov = maisbaraton = 0
print("-"*70)
print("{:^70}".format("FRIGOR HANS"))
print("-"*70)
while True:
    preco = escolha = ' '
    qntd += 1
    nome = str(input("Nome do Produto:  ")).strip().upper()
    while not isinstance(preco, float):
        preco = input("Preço do Produto: R$")
        try:
            preco = float(preco)
            if preco < 0:
                preco = ' '
                print("Você não digitou um valor válido, tente novamente!")
            break
        except ValueError:
            print("Você não digitou um valor válido, tente novamente!")
    if qntd == 1 or preco < maisbaratov:
        maisbaratov = preco
        maisbaraton = nome
    total += preco
    if preco > 1000:
        prodcaro += 1
    while escolha not in "SN":
        escolha = str(input("Voce deseja continuar [S/N]? ")).upper().strip()[0]
        if escolha not in "SN":
            print("Você selecionou uma opção inválida, tente novamente!")
    if escolha in "N":
        print("{:-^70}".format(" Fim do Programa! "))
        break
print(f"O total da compra foi R${total:.2f} para adiquirir {qntd} produtos.\n"
      f"{prodcaro} destes produtos valem mais de um barão!\n"
      f"O produto mais barato adiquirido foi {maisbaraton} que custou R${maisbaratov:.2f}")
