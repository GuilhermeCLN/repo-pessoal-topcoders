import json
path = (r'C:\Users\Guilerme\Repositórios de códigos\repo-pessoal-topcoders\Projetos\banco_de_dados.json')

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
    print(type(lista_dicts))
    lista_dicts.append(dict_cadastro)
    return lista_dicts

def carregar_json(path:str):
    with open(path, 'r') as arquivo:
        lista_dicts = json.load(arquivo)
    return lista_dicts

lista_dicts = carregar_json(path)
lista_dicts_att = cadastrar_musicos('teste', 'teste 2', 'teste', 'teste', lista_dicts)
print(lista_dicts_att)