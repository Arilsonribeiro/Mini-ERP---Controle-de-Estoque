from idlelib.iomenu import encoding

from lib.interface import*
from datetime import datetime


def arquivoExiste(nome):
    try:
        a = open(nome,'rt',encoding="utf-8") #abrir o rquivo e ler
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
     try:
        a = open(nome,'wt+',encoding="utf-8")
        a.close()
     except:
        print('\033[31mHouve um erro na criação do arquivo\033[m')
     else:
        print(f'\033[32mArquivo {nome} criado com sucesso\033[m')




def lerArquivo(nome):
    try:
        a = open(nome, 'rt',encoding='utf-8')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('\033[32mMateriais Cadastrados\033[m')
        print(f'{"\033[33mNome do Produto":<25} {"Codigo":<10}{"Lote":<10}{"local":<10}{"Status":<10}{"Data/Hora Entrada":>25}\033[m')

        for linha in a:
            if linha.strip():
                dado = linha.strip().split(';')

                if len(dado) >= 6:
                    codigo = dado[1]
                    nome_prod = dado[0]
                    lote = dado[2]
                    local = dado[3]
                    status= dado[4]
                    data_ent = dado[5].strip()  # <--- Aqui pegamos o horário real do arquivo!

                    # Exibe cada produto com seu respectivo horário individual
                    print(f'{nome_prod:<20}{codigo:<10}{lote:<10}{local:<10}{status:<10} {data_ent:>26}')

        a.close()




def cadastrar (arq,codigo=0,nome='Desconhecido', lote=0,status='N/A', local=000):
    data_entrada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    try:
        a = open(arq,'at',encoding='utf-8')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{codigo};{nome};{lote};{local};{status};{data_entrada} \n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print()
            print('\033[32m Material Cadastrado com sucesso!\033[m')
            print(f'\033[32m Novo registro de {nome} adicionado {data_entrada}.\033[m')
            a.close()


def stock_check (arq, codigo_remover):
    try:
        # 1. Lê todas as linhas do arquivo
        a = open(arq, 'rt', encoding='utf-8')
        linhas = a.readlines()
        a.close()

        linhas_restantes = []
        encontrado = False

        # 2. Procura o material linha por linha
        for linha in linhas:
            if linha.strip():
                dado = linha.strip().split(';')

                codigo_atual = dado[1].strip()
                codigo_busca = str(codigo_remover).strip()


                if codigo_atual == codigo_busca:
                    print(f'\033[31m Stock Check do produto: {dado[0].strip()} {dado[1]}\033[m')
                    encontrado = True
                else:
                    linhas_restantes.append(f"{linha.strip()}\n")

        # 3. Se não achou ninguém, avisa o usuário
        if not encontrado:
            print('\033[31mmaterial não encontrado\033[m')
        else:
            # 4. Só reescreve o arquivo se algo realmente mudou
            a = open(arq, 'wt', encoding='utf-8')
            a.writelines(linhas_restantes)
            a.close()

    except:
        print('Erro ao processar o arquivo.')