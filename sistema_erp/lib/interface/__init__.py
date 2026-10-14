def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor digite uma opção válida')
            continue
        except (KeyboardInterrupt):
            print('Usuário não digitou uma opção')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' *tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu (lista):
    cabeçalho('SISTEMA ERP')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc = leiaInt('Digite uma opção:')
    return opc