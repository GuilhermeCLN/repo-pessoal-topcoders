import json

def carregar_json(path:str):
    with open(path, 'r') as arquivo:
        lista_dicts = json.load(arquivo)
    return lista_dicts

def salvar_json(path:str, lista_dicts:list)->None:
    string_json = json.dumps(lista_dicts)
    with open(path, 'w') as arquivo:
        arquivo.write(string_json)
    return None

def cadastrar_musicos(nome:str, email:str, generos:list, instrumentos:list, lista_dicts:list):
    for dict in lista_dicts:
        if dict['email'] == email:
            raise Exception('Usuário já cadastrado no sistema.')
    dict_cadastro = {
                    'nome' : nome, 
                    'email': email, 
                    'generos' : generos, 
                    'instrumentos' : instrumentos
                    }
    lista_dicts.append(dict_cadastro)
    return lista_dicts

def buscar_musicos(lista_dicts:list, ou:bool, nome:str = None, email:str = None, generos:str = None, instrumentos:str = None):
    if ou == 0:
        lista_consulta = lista_dicts.copy()
        if email:
            for dict in lista_consulta:
                if dict['email'] != email:
                    lista_consulta.pop(lista_consulta.index(dict))
        else:
            if nome:
                for dict in lista_dicts:
                    if dict['nome'] != nome:
                        lista_consulta.pop(lista_consulta.index(dict))
            if generos:
                for dict in lista_dicts:
                    if generos not in dict['generos']:
                        lista_consulta.pop(lista_consulta.index(dict))
            if instrumentos:
               for dict in lista_dicts:
                    if instrumentos not in dict['instrumentos']:
                        lista_consulta.pop(lista_consulta.index(dict)) 
    elif ou == 1:
        lista_consulta = []
        if email:
            for dict in lista_consulta:
                if dict['email'] == email:
                    lista_consulta.append(dict)
        else:
            if nome:
                for dict in lista_dicts:
                    if dict['nome'] == nome:
                        lista_consulta.append(dict)
            if generos:
                for dict in lista_dicts:
                    if generos in dict['generos']:
                        lista_consulta.append(dict)
            if instrumentos:
               for dict in lista_dicts:
                    if instrumentos in dict['instrumentos']:
                        lista_consulta.append(dict)        
    return lista_consulta

def modificar_musicos( lista_dicts:list, email:str, remover:bool, generos:list = None, instrumentos:list = None):
    for dict in lista_dicts:
        if dict['email'] != email:
            if remover:
                if generos:
                    for genero in generos:
                        dict['generos'].remove(genero)
                if instrumentos:
                    for instrumento in instrumentos:
                        dict['instrumentos'].remove(instrumento)
            elif not remover:
                if generos:
                    for genero in generos:
                        dict['generos'].append(genero)
                if instrumentos:
                    for instrumento in instrumentos:
                        dict['instrumentos'].append(instrumento)
    return lista_dicts

def input_cadastro():
    certo = False
    while certo == False:
        nome = str(input('Por favor, digite o nome do músico, contendo apenas letras e espaço.')).lower()
        certo = True
        for letra in nome:
            if letra.isalpha() == False and letra != ' ':
                print('Por favor, digite um nome válido, contendo apenas letras e espaços.')
                certo = False
                break

    certo = False
    while certo == False:
        email = str(input('Por favor, digite o email do músico. O email deve conter apenas letras, underscore (_), ponto (.), dígitos numéricos e, obrigatoriamente, exatamente 1 arroba.')).lower()
        certo = True
        for letra in email:
            if letra.isalnum() == False and letra not in ['_', '.', '@']:
                print('Por favor, digite um email válido, contendo apenas letras, underscore (_), ponto (.), dígitos numéricos e, obrigatoriamente, exatamente 1 arroba.')
                certo = False
                break
        if email.count('@') != 1:
            print('Por favor, digite um email válido, contendo apenas letras, underscore (_), ponto (.), dígitos numéricos e, obrigatoriamente, exatamente 1 arroba.')
            certo = False
    
    instrumentos = []
    while instrumentos == []:
        instrumentos = str(input('Por favor, digite os instrumentos tocados pelo músico separados por vírgulas.')).lower().split(',')

    generos = []
    while generos == []:
        generos = str(input('Por favor, digite os gêneros tocados pelo músico separados por vírgulas.')).lower().split(',')

    return nome, email, instrumentos, generos

def input_cadastro():
    certo = False
    while certo == False:
        nome = str(input('Por favor, digite o nome do músico, contendo apenas letras e espaço.')).lower()
        certo = True
        for letra in nome:
            if letra.isalpha() == False and letra != ' ':
                print('Por favor, digite um nome válido, contendo apenas letras e espaços.')
                certo = False
                break

    certo = False
    while certo == False:
        email = str(input('Por favor, digite o email do músico. O email deve conter apenas letras, underscore (_), ponto (.), dígitos numéricos e, obrigatoriamente, exatamente 1 arroba.')).lower()
        certo = True
        for letra in email:
            if letra.isalnum() == False and letra not in ['_', '.', '@']:
                print('Por favor, digite um email válido, contendo apenas letras, underscore (_), ponto (.), dígitos numéricos e, obrigatoriamente, exatamente 1 arroba.')
                certo = False
                break
        if email.count('@') != 1:
            print('Por favor, digite um email válido, contendo apenas letras, underscore (_), ponto (.), dígitos numéricos e, obrigatoriamente, exatamente 1 arroba.')
            certo = False

    instrumentos = []
    while instrumentos == []:
        instrumentos = str(input('Por favor, digite os instrumentos tocados pelo músico separados por vírgulas.')).lower().split(',')

    generos = []
    while generos == []:
        generos = str(input('Por favor, digite os gêneros tocados pelo músico separados por vírgulas.')).lower().split(',')

    return nome, email, instrumentos, generos

def input_busca():
    ou = 3
    while ou != True and ou != False:
        ou = bool(input('Você deseja fazer uma busca exata ou geral? Escolha o número correspondente.\n'
                        '0. Busca exata\n'
                        '1. Busca parcial\n'))
    nome, email, genero, instrumento = None, None, None, None
    while nome == None and email == None and genero == None and instrumento == None:
        nome = str(input('Digite o nome do músico. Caso não deseje utilizar este parâmetro, apenas digite enter.')).lower()
        if nome == '':
            nome = None
        email = str(input('Digite o email do músico. Caso não deseje utilizar este parâmetro, apenas digite enter.')).lower()
        if email == '':
            email = None
        genero = str(input('Digite o genero do músico. Caso não deseje utilizar este parâmetro, apenas digite enter.')).lower()
        if genero == '':
            genero = None
        instrumento = str(input('Digite o instrumento do músico. Caso não deseje utilizar este parâmetro, apenas digite enter.')).lower()
        if instrumento == '':
            instrumento = None
        if nome == None and email == None and genero == None and instrumento == None:
            print('Por favor, escolha pelo menos um dos parâmetros de busca.')
    
    return ou, nome, email, genero, instrumento

def input_mudanca():
    remover = 3
    while remover != True and remover != False:
        remover = bool(input('Você deseja remover ou adicionar dados? Escolha a opção concernente.\n'
                            '0. Adicionar\n'
                            '1. Remover\n'))
        if remover != True and remover != False:
            print('Por favor, escolha uma opção válida.')
    
    email = ''
    while email == '':
        email = str(input('Por favor, digite o email do músico a ser modificado.')).lower()
    
    while generos == None and instrumentos == None:
        generos = str(input('Digite os generos a serem adicionados ou removidos separados por virgula. Caso não deseje utilizar este parâmetro, apenas digite enter.')).lower()
        if generos == '':
            generos = None
        instrumentos = str(input('Digite o instrumentos a serem adicionados ou removidos separados por virgula. Caso não deseje utilizar este parâmetro, apenas digite enter.')).lower()
        if instrumentos == '':
            instrumentos = None
        if generos == None and instrumentos == None:
            print('Por favor, escolha pelo menos um dos dados a serem modificados.')

    return remover, email, generos, instrumentos

def printer(resultado)-> None:
    '''
    Esta função recebe o resultado apontado pela função menu e imprime em um layout mais amigável ao usuário.
    '''
    if type(resultado) == list:
        for item in resultado:
            if type(item) == dict:
                    print(f'Nome:{item["nome"]} | Email: {item["email"]} | generos: {*item["generos"],}, | instrumentos: {*item["instrumentos"],}\n')
            else:
                    print(f'Categoria {resultado.index(item)+1}: {item}')

    elif type(resultado) == dict:
        print(f'ID: {resultado["id"]} | Preço: {resultado["preco"]} | Categoria: {resultado["categoria"]}\n')

    return None

def menu(path) -> None:
    '''
    Esta função recebe os dados de produtos em forma de lista de dicionários e coleta a opção desejada pelo usuário, chamando as funções corretas para executar a demanda.
    '''

    n = -1

    print('Olá, seja bem vindo ao organizador de bandas!')
    while n != '0':
        n = input('\nEscolha uma das opções abaixo e digite o número de referência.\n'
                    '\n'
                    '1. Cadastrar músicos\n'
                    '2. Buscar músicos\n'
                    '3. Modificar músicos\n'
                    '4. Montar bandas\n'
                    '0. Sair\n')
                    
        lista_dicts = carregar_json(path)

        if n == '1':
            nome, email, instrumentos, generos = input_cadastro()
            cadastrar_musicos(nome, email, generos, instrumentos, lista_dicts)

        elif n == '2':
            ou, nome, email, genero, instrumento = input_busca()
            lista_busca = buscar_musicos(lista_dicts, ou, nome = nome, email = email, generos = genero, instrumentos = instrumento)
            printer(lista_busca)

        elif n == '3':
            remover, email, generos, instrumentos = input_mudanca()
            modificar_musicos(lista_dicts, email, remover, generos = generos, instrumentos = instrumentos)

        elif n == '4':
            printer()

        elif n == '0':
            print('Até a próxima!')
            break
        
        salvar_json(path, lista_dicts)

#criar arquivo e chamar o menu

path = (r'C:\Users\Guilerme\Repositórios de códigos\repo-pessoal-topcoders\Projetos\banco_de_dados.json')
menu(path)


