x = input("Digite algo: ")
print("O que digitou é do tipo: {}.\n É Alpha-númerico? {}\n É númerico? {}\n É alfabeto? {}\n É decimal? {}\n"
      " É dígito? {}\n É identificador? {}\n É minúsculo? {}\n É imprimível? {}\n É espaço? {}\n É título? {}\n"
      " É maiúsculo? {}"
      .format(type(x), x.isalnum(), x.isnumeric(), x.isalpha(), x.isdecimal(), x.isdigit(), x.isidentifier(),
              x.islower(), x.isprintable(), x.isspace(), x.istitle(), x.isupper()
              )
      )
