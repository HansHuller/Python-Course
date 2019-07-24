'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final mostre:
Quantas pessoas têm mais de 18 anos.
Quantos homens foram cadastrados.
Quantas mulheres têm menos de 20 anos.
'''
pessoasmaiores = homens = mulheresmenores = 0
print("="*80)
print("{:=^80}".format("Bem vindo ao programa de cadastro de usuários!"))
print("="*80)
while True:
    print("-"*80)
    print("{:-^80}".format("Cadastre uma pessoa"))
    print("-" * 80)
    continuar = idade = sexo = ''
    while not isinstance(idade, int):
        idade = input("Idade:      ")
        try:
            idade = int(idade)
            if idade < 0:
                idade = ''
                print("Você não digitou uma idade válida, tente novamente!")
            break
        except ValueError:
            print("Você não digitou uma idade válida, tente novamente!")
    while sexo != "M" and sexo != "F":
        sexo = str(input("Sexo [F/M]: ")).strip().upper()[0]
        if sexo != "M" and sexo != "F":
            print("Você não digitou uma opção válida, tente novamente!")
    if idade >= 18:
        pessoasmaiores += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheresmenores += 1
    print("-" * 80)
    while continuar != "S" and continuar != "N":
        continuar = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]
    if continuar == "N":
        break
print("-" * 80)
print(f"Você cadastrou  {pessoasmaiores} maiores de idade.\n"
      f"Destas {homens} são homens.\n"
      f"E {mulheresmenores} são mulheres com menos de 20 anos.")
