import ex115module.functionalities.data as dv

def menu():
    dv.titulo("MENU PRINCIPAL")
    print("\033[33m1 - \033[m\033[34mVer pessoas cadastradas\033[m")
    print("\033[33m2 - \033[m\033[34mCadastrar nova Pessoa\033[m")
    print("\033[33m3 - \033[m\033[34mSair do Sitema\033[m")
    return dv.choose()
