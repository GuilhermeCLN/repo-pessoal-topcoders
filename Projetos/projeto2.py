import json

def carregar_json(path:str):
    '''
        Carrega o json já existente no path.
    '''
    with open(path, 'r') as arquivo:
        lista_dicts = json.load(arquivo)
    return lista_dicts

def salvar_json(path:str, lista_dicts:list)->None:
    '''
        Salva alterações realizadas em um json no path.
    '''
    string_json = json.dumps(lista_dicts)
    with open(path, 'w') as arquivo:
        arquivo.write(string_json)
    return None

def cadastrar_musicos(nome:str, email:str, generos:list, instrumentos:list, lista_dicts:list):
    '''
        Cadastra novos músicos no banco de dados, com os campos de nome, email, gêneros e instrumentos.
    '''
    for dict in lista_dicts:
        if dict['email'] == email:
            raise Exception('Usuário já cadastrado no sistema')
    dict_cadastro = {
                    'nome' : nome, 
                    'email': email, 
                    'generos' : generos, 
                    'instrumentos' : instrumentos
                    }
    lista_dicts.append(dict_cadastro)
    return lista_dicts

def buscar_musicos(lista_dicts:list, ou:str, nome:str = None, email:str = None, generos:str = None, instrumentos:str = None):
    '''
        Realiza buscas personalizadas no banco de dados.
    '''
    if ou == '0':
        lista_consulta = lista_dicts.copy()
        if email:
            i = 0
            while i < len(lista_consulta):
                if lista_consulta[i]['email'] != email:
                    lista_consulta.pop(i)
                    i -= 1
                i += 1
        else:
            if nome:
                i = 0
                while i < len(lista_consulta):
                    if lista_consulta[i]['nome'] != nome:
                        lista_consulta.pop(i)
                        i -= 1
                    i += 1
            if generos:
                i = 0
                while i < len(lista_consulta):
                    if generos not in lista_consulta[i]['generos']:
                        lista_consulta.pop(i)
                        i -= 1
                    i += 1
            if instrumentos:
                i = 0
                while i < len(lista_consulta):
                    if instrumentos not in lista_consulta[i]['instrumentos']:
                        lista_consulta.pop(i)
                        i -= 1
                    i += 1
        if not lista_consulta:
            raise Exception('Nenhum valor encontrado')

    elif ou == '1':
        lista_consulta = []
        if email:
            for dict in lista_dicts:
                if dict['email'] == email:
                    lista_consulta.append(dict)
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

        if not lista_consulta:
            raise Exception('Nenhum valor encontrado')

    return lista_consulta

def modificar_musicos(lista_dicts:list, email:str, remover:str, generos:list = None, instrumentos:list = None):
    '''
        Realiza modificações no banco de dados tocantes aos gêneros e instrumentos tocados por um determinado músico.
    '''
    achou = False
    for dict in lista_dicts:
        if dict['email'] == email:
            achou = True
            if remover =='1':
                if generos:
                    for genero in generos:
                        dict['generos'].remove(genero)
                if instrumentos:
                    for instrumento in instrumentos:
                        dict['instrumentos'].remove(instrumento)
            elif remover =='0':
                if generos:
                    for genero in generos:
                        dict['generos'].append(genero)
                if instrumentos:
                    for instrumento in instrumentos:
                        dict['instrumentos'].append(instrumento)
    if achou == False:
        raise Exception('Nenhum músico encontrado para o email fornecido')
    
    return lista_dicts

def montar_bandas(lista_dicts:list, genero:str, n_musicos:int, instrumentos:list):
    '''
        Monta bandas com todas as possibilidades de músicos presentes no banco de dados, de acordo com o genero, número de componentes da banda e instrumentos tocados.
    '''
    possibilidades = []
    for instrumento in instrumentos:
        lista_consulta = buscar_musicos(lista_dicts, '0', generos= genero, instrumentos= instrumento)
        for dict in lista_consulta:
            possibilidades.append([dict['email'], instrumento])
    
    return realizar_combinações(possibilidades, n_musicos)

def realizar_combinações(possibilidades:list,n_musicos:int) ->list:
    '''
        Gera uma lista com todas as combinações possíveis não repetidas para um certo conjunto de possibilidades.
    '''
    combinações_gerais = combinar(possibilidades, n_musicos)
    lista_final = []

    for k in combinações_gerais:
        lista_repetidos = []
        lista_repetidos2 = []
        repetido = False

        for j in k:
            if j[1] in lista_repetidos or j[0] in lista_repetidos2: 
                repetido = True
                break
            lista_repetidos.append(j[1])
            lista_repetidos2.append(j[0])

        if repetido == False:
            lista_final.append(k)
    
    return lista_final

def combinar(possibilidades:list, n_musicos:int):
    '''
        Realiza as combinações com repetição para um certo conjunto de possibilidades utilizando recursão.
    '''
    if n_musicos == 0:
        return [[]]

    combinações_gerais = []
    for j in range(len(possibilidades)):
        for i in combinar(possibilidades[j+1:], n_musicos-1):
            combinações_gerais.append([possibilidades[j], *i])

    return combinações_gerais

def input_cadastro():
    '''
        Recebe e valida os inputs relacionados à função de cadastro dos músicos.
    '''
    certo = False
    while certo == False:
        nome = str(input('Por favor, digite o nome do músico, contendo apenas letras e espaço.\n')).lower()
        certo = True
        for letra in nome:
            if letra.isalpha() == False and letra != ' ':
                print('Por favor, digite um nome válido, contendo apenas letras e espaços.\n')
                certo = False
                break

    certo = False
    while certo == False:
        email = str(input('Por favor, digite o email do músico. O email deve conter apenas letras, underscore (_), ponto (.), dígitos numéricos e, obrigatoriamente, exatamente 1 arroba.\n')).lower()
        certo = True
        for letra in email:
            if letra.isalnum() == False and letra not in ['_', '.', '@']:
                print('Por favor, digite um email válido, contendo apenas letras, underscore (_), ponto (.), dígitos numéricos e, obrigatoriamente, exatamente 1 arroba.\n')
                certo = False
                break
        if email.count('@') != 1:
            print('Por favor, digite um email válido, contendo apenas letras, underscore (_), ponto (.), dígitos numéricos e, obrigatoriamente, exatamente 1 arroba.\n')
            certo = False

    instrumentos = []
    while instrumentos == []:
        instrumentos_input = str(input('Por favor, digite os instrumentos tocados pelo músico separados por vírgulas.\n')).lower().split(',')
        instrumentos = [item.strip() for item in instrumentos_input]

    generos = []
    while generos == []:
        generos_input = str(input('Por favor, digite os gêneros tocados pelo músico separados por vírgulas.\n')).lower().split(',')
        generos = [item.strip() for item in generos_input]

    return nome, email, instrumentos, generos

def input_busca():
    '''
        Recebe e valida os inputs relacionados à função de busca dos músicos.
    '''
    ou = 'vazio'
    while ou != '0' and ou != '1':
        ou = input('Você deseja fazer uma busca exata ou geral? Escolha o número correspondente.\n'
                        '0. Busca exata\n'
                        '1. Busca geral\n')
    nome, email, genero, instrumento = None, None, None, None
    while nome == None and email == None and genero == None and instrumento == None:
        email = str(input('Digite o email do músico. Caso não deseje utilizar este parâmetro, apenas digite enter.\n')).lower()
        if email == '':
            email = None
        elif email != '' and ou == '0':
            continue
        nome = str(input('Digite o nome do músico. Caso não deseje utilizar este parâmetro, apenas digite enter.\n')).lower()
        if nome == '':
            nome = None
        genero = str(input('Digite o genero do músico. Caso não deseje utilizar este parâmetro, apenas digite enter.\n')).lower()
        if genero == '':
            genero = None
        instrumento = str(input('Digite o instrumento do músico. Caso não deseje utilizar este parâmetro, apenas digite enter.\n')).lower()
        if instrumento == '':
            instrumento = None
        if nome == None and email == None and genero == None and instrumento == None:
            print('Por favor, escolha pelo menos um dos parâmetros de busca.')
    
    return ou, nome, email, genero, instrumento

def input_mudanca():
    '''
        Recebe e valida os inputs relacionados à função de mudança de dados dos músicos.
    '''
    remover = 3
    while remover != '0' and remover != '1':
        remover = str(input('Você deseja remover ou adicionar dados? Escolha a opção concernente.\n'
                            '0. Adicionar\n'
                            '1. Remover\n'))
        if remover != '0' and remover != '1':
            print('Por favor, escolha uma opção válida.')
    
    email = ''
    while email == '':
        email = str(input('Por favor, digite o email do músico a ser modificado.\n')).lower()
    
    generos, instrumentos = None, None

    while generos == None and instrumentos == None:
        generos_input = str(input('Digite os gêneros a serem adicionados ou removidos separados por virgula. Caso não deseje utilizar este parâmetro, apenas digite enter.\n')).lower().split(',')
        if generos_input == '':
            generos = None
        else:
            generos = [item.strip() for item in generos_input]
        instrumentos_input = str(input('Digite o instrumentos a serem adicionados ou removidos separados por virgula. Caso não deseje utilizar este parâmetro, apenas digite enter.\n')).lower().split(',')
        if instrumentos_input == '':
            instrumentos = None
        else:
            instrumentos = [item.strip() for item in instrumentos_input] 
        if generos == None and instrumentos == None:
            print('Por favor, escolha pelo menos um dos dados a serem modificados.\n')

    return remover, email, generos, instrumentos

def input_montagem():
    '''
        Recebe e valida os inputs relacionados à função de montagem de bandas.
    '''
    genero = ''
    while genero == '':
        genero = input('Por favor, digite o gênero musical da banda: ').lower()
    n_musicos = ''
    while n_musicos == '':
        n_musicos = int(input('Por favor, digite a quantidade desejada de integrantes: '))
    instrumentos = []

    for i in range(n_musicos):
        instrumentos.append(input(f"Digite o instrumento do {i+1}º músico: ").lower())
    
    return genero, n_musicos, instrumentos

def printer(resultado)-> None:
    '''
    Esta função recebe o resultado apontado pela função menu e imprime em um layout mais amigável ao usuário.
    '''
    if type(resultado) == list:
        for item in resultado:
            if type(item) == dict:
                    print(f'Nome:{item["nome"]} | Email: {item["email"]} | Generos: {*item["generos"],}, | Instrumentos: {*item["instrumentos"],}\n')
            elif type(item) == list:
                    print(' + '.join(str(f'Email:{x[0]} | Instrumento {x[1]}') for x in item))
            else:
                print('Desculpe, um erro foi encontrado.')
                break
    
    else:
        print('Desculpe, um erro foi encontrado.')

    return None

def menu(path) -> None:
    '''
    Esta função recebe o path do arquivo do banco de dados em forma de json e coleta a opção desejada pelo usuário, chamando as funções corretas para executar a demanda.
    '''
    lista_dicts = carregar_json(path)

    print('Olá, seja bem vindo ao organizador de bandas!')
    n = -1
    while n != '0':
        n = input('\nEscolha uma das opções abaixo e digite o número de referência.\n'
                    '\n'
                    '1. Cadastrar músicos\n'
                    '2. Buscar músicos\n'
                    '3. Modificar músicos\n'
                    '4. Montar bandas\n'
                    '0. Sair\n')

        if n == '1':
            try:
                nome, email, instrumentos, generos = input_cadastro()
                cadastrar_musicos(nome, email, generos, instrumentos, lista_dicts)
                print ('Dados cadastrados com sucesso')
            except:
                print('O usuário já está cadastrado no sistema.')

        elif n == '2':
            try:
                ou, nome, email, genero, instrumento = input_busca()
                lista_busca = buscar_musicos(lista_dicts, ou, nome = nome, email = email, generos = genero, instrumentos = instrumento)
                print ('Resultado da busca:\n')
                printer(lista_busca)
            except:
                print('Desculpe! Nenhum valor foi encontrado para os parâmetros fornecidos na busca. Tente novamente com outros parâmetros.')

        elif n == '3':
            #try:
            remover, email, generos, instrumentos = input_mudanca()
            modificar_musicos(lista_dicts, email, remover, generos = generos, instrumentos = instrumentos)
            print ('Dados modificados com sucesso')
            #except:
                #print('Não foram encontrados músicos para o email fornecido. Por favor cheque o email e tente novamente.')

        elif n == '4':
            try:
                genero, n_musicos, instrumentos = input_montagem()
                lista_montagem = montar_bandas(lista_dicts, genero, n_musicos, instrumentos)
                printer(lista_montagem)
            except:
                print('\nNão foi possível montar as bandas com os parâmetros fornecidos. Por favor, revise os parâmetros e tente novamente.')

        elif n == '0':
            print('Até a próxima!')
            break
        
        salvar_json(path, lista_dicts)

#criar arquivo e chamar o menu
path = ('banco_de_dados.json')
try:
    menu(path)

except FileNotFoundError:
    with open(path, 'w') as arquivo:
        lista_dicts_in = []
        json_string = json.dumps(lista_dicts_in)
        arquivo.write(json_string)
    menu(path)