import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    Esta função recebe os dados de produtos em forma de lista de dicionários e retorna todas as categorias de produtos.   
    '''
    lista_cat = []
    for dic in dados:
        if dic['categoria'] not in lista_cat:
            lista_cat.append(dic['categoria'])
    return lista_cat

def listar_por_categoria(dados, categoria):
    '''
    Esta função recebe os dados de produtos em forma de lista de dicionários e uma categoria em forma de string, retornando uma lista todos os produtos presentes na categoria de referência.
    '''
    lista_prod_cat = []
    for dic in dados:
        if dic['categoria'] == categoria:
            lista_prod_cat.append(dic)
    return lista_prod_cat

def produto_mais_caro(dados, categoria):
    '''
    Esta função recebe os dados de produtos em forma de lista de dicionários e uma categoria em forma de string, retornando um dicionário contendo o produto mais caro na categoria de referência.
    '''
    lista_prod_cat = listar_por_categoria(dados, categoria)
    prod_mais_caro = sorted(lista_prod_cat, key = lambda x: float(x['preco']), reverse = True)[0]
    return prod_mais_caro

def produto_mais_barato(dados, categoria):
    '''
    Esta função recebe os dados de produtos em forma de lista de dicionários e uma categoria em forma de string, retornando um dicionário contendo o produto mais barato na categoria de referência.
    '''
    lista_prod_cat = listar_por_categoria(dados, categoria)
    prod_mais_barato = sorted(lista_prod_cat, key = lambda x: float(x['preco']))[0]
    return prod_mais_barato

def top_10_caros(dados):
    '''
    Esta função recebe os dados de produtos em forma de lista de dicionários e retorna uma lista de dicionários contendo os 10 produtos mais caros.
    '''
    podio_caros = sorted(dados, key = lambda x: float(x['preco']), reverse = True)[0:9]
    return podio_caros

def top_10_baratos(dados):
    '''
    Esta função recebe os dados de produtos em forma de lista de dicionários e retorna uma lista de dicionários contendo os 10 produtos mais baratos.
    '''
    podio_baratos = sorted(dados, key = lambda x: float(x['preco']))[0:9]
    return podio_baratos

def validar_categoria(categoria):
    '''
    Esta função recebe uma categoria em forma de string, realizando a conferência se a categoria se encontra dentre as disponíveis, retornando, ao final, uma categoria necessariamente válida.
    '''
    lista_cat = listar_categorias(dados)
    while categoria not in lista_cat:
        categoria = input('Categoria inválida! Por favor, tente de novo. Digite uma nova categoria, ou, caso deseje retornar ao menu, digite 0:')
        if categoria == '0':
            break
    return categoria

def menu(dados) -> None:
    '''
    Esta função recebe os dados de produtos em forma de lista de dicionários e coleta a opção desejada pelo usuário, chamando as funções corretas para executar a demanda.
    '''
    opcoes = {
    '1': listar_categorias,
    '2': listar_por_categoria,
    '3': produto_mais_caro,
    '4': produto_mais_barato,
    '5': top_10_caros,
    '6': top_10_baratos}

    def default(dados = None, categoria = None) -> None:
        '''
        Esta função é executada pela função "get" caso a opção do menu escolhida pelo usuário não exista.
        '''
        print ('Opção inválida! Por favor, tente de novo.')
    
    def chamador(n, dados, categoria = None):
        '''
        Esta função chama a função correta dentro do dicionário de opções para executar a demanda do usuário.
        '''
        if n == '2' or n == '3' or n == '4':
            resultado = opcoes[n](dados, categoria)
        else:
            resultado = opcoes.get(n, default)(dados)

        return resultado
    
    def printer(resultado):
        '''
        Esta função recebe o resultado apontado pela função chamador e imprime em um layout mais amigável ao usuário.
        '''
        if type(resultado) == list:
            for item in resultado:
                if type(item) == dict:
                    print(f'ID:{item["id"]} | Preço: {item["preco"]} | Categoria: {item["categoria"]}\n')
                else:
                    print(f'Categoria {resultado.index(item)+1}: {item}')

        elif type(resultado) == dict:
            print(f'ID: {resultado["id"]} | Preço: {resultado["preco"]} | Categoria: {resultado["categoria"]}\n')

    n = -1

    print('Olá, seja bem vindo ao menu de análise dos dados de produto!')
    while n != '0':
        n = input('\nEscolha uma das opções abaixo e digite o número de referência.\n'
                    '\n'
                    '1. Listar categorias\n'
                    '2. Listar produtos de uma categoria\n'
                    '3. Produto mais caro por categoria\n'
                    '4. Produto mais barato por categoria\n'
                    '5. Top 10 produtos mais caros\n'
                    '6. Top 10 produtos mais baratos\n'
                    '0. Sair\n')

        if n == '2' or n == '3' or n == '4':
            categoria = input('Por favor, escolha uma categoria:\n').lower()
            categoria = validar_categoria(categoria)
            resultado = chamador(n, dados, categoria)
            printer(resultado)

        elif n == '0':
            print('Até a próxima!')
            break
        
        else:
            resultado = chamador(n, dados)
            printer(resultado)

# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)