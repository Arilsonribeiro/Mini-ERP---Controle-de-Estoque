from lib.interface import *
from lib.arquivo import *
from time import time, sleep

arq = 'materiais.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    # menu está dentro de interface
    resposta = menu (['Cadastrar Material','Vizualizar Materiais','Stock check','Sair'])
    if resposta == 1:
        while True:
            cabeçalho('Novo Material')
            codigo = input("Código: ")
            nome = str(input('Nome: ')).upper()
            lote = input('Lote: ')
            status = input('Status: ').upper()
            local = input('Local de Armazenamento: ').upper()
            cadastrar(arq,nome,codigo,lote,status,local)
            sleep(1)
            resp = str(input('Deseja cadastrar outro? [S/N]: ')).strip().upper()
            if resp == 'N':
                break

    elif resposta == 2:
        lerArquivo('materiais.txt')



    elif resposta == 3:
        print()
        print('\033[31mStock Check\033[m'.center(42))
        lerArquivo('materiais.txt')
        print()
        cod = input('Digite o código do produto para o Stock Check: ')
        stock_check('materiais.txt',cod)



    elif resposta == 4:
        cabeçalho('\033[34mSaindo do Siatema!\033[m')
        break

