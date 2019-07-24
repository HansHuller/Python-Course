# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n1 = int(input("Digite o número cuja taboada você deseja: "))
print("-"*12,"\n{:>2} * {:>2} = {:>4}\n{:>2} * {:>2} = {:>4}\n{:>2} * {:>2} = {:>4}\n{:>2} * {:>2} = {:>4}\n{:>2} * {:>2} = {:>4}\n"
      "{:>2} * {:>2} = {:>4}\n{:>2} * {:>2} = {:>4}\n{:>2} * {:>2} = {:>4}\n{:>2} * {:>2} = {:>4}\n{:>2} * {:>2} = {:>4}\n"
      .format(n1, 1, 1*n1,n1, 2, 2*n1,n1, 3, 3*n1, n1, 4, 4*n1, n1, 5, 5*n1, n1, 6,
              6*n1, n1, 7, 7*n1, n1, 8, 8*n1, n1, 9, 9*n1, n1, 10, 10*n1
              ),"-"*12
      )
