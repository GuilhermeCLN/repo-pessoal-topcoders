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
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    lista_cat = []
    for dic in dados:
        if dic['categoria'] not in lista_cat:
            lista_cat.append(dic['categoria'])
    return lista_cat

def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    lista_prod_cat = []
    for dic in dados:
        if dic['categoria'] == categoria:
            lista_prod_cat.append(dic)
    return lista_prod_cat


def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    lista_prod_cat = listar_por_categoria(dados, categoria)
    prod_mais_caro = sorted(lista_prod_cat, key = lambda x: float(x['preco']), reverse = True)[0]
    return prod_mais_caro


def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais barato da categoria dada.
    '''
    lista_prod_cat = listar_por_categoria(dados, categoria)
    prod_mais_barato = sorted(lista_prod_cat, key = lambda x: float(x['preco']))[0]
    return prod_mais_barato

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    podio_caros = sorted(dados, key = lambda x: float(x['preco']), reverse = True)[0:9]
    return podio_caros

def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''
    podio_baratos = sorted(dados, key = lambda x: float(x['preco']))[0:9]
    return podio_baratos

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    n = 1
    while n != '0':
        n = input('Olá, seja bem vindo ao menu de análise dos dados de produto! Escolha uma das opções abaixo e digite o número de referência.\n'
                    '1. Listar categorias\n'
                    '2. Listar produtos de uma categoria\n'
                    '3. Produto mais caro por categoria\n'
                    '4. Produto mais barato por categoria\n'
                    '5. Top 10 produtos mais caros\n'
                    '6. Top 10 produtos mais baratos\n'
                    '0. Sair\n'
                )
        if n == 1


# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)
