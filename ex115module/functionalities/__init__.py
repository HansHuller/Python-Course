from ex115module.functionalities import menu, listar, cadastrar, data


def miniSystem():
    teste = 0
    while teste != 3:
        teste = menu.menu()
    print("-"*70)
    print(f"{'FIM DO PROGRAMA':^70}")
    print("-" * 70)
