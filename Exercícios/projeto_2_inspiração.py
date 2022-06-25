import csv
import os.path

def arquivo():
    file_exists = os.path.exists('cadastro.csv')
    if file_exists == False:
        file = open('cadastro.csv','w+')
        escrita=csv.DictWriter(file,skipinitialspace=True,delimiter=';', lineterminator='\n',fieldnames=header)
        escrita.writeheader()
        escrita.writerows(lista_modifica)
    else:
        file = open('cadastro.csv','a+')
        
def check_email(email):
    arquivo = open('cadastro.csv', 'r')
    planilha = list(csv.reader(arquivo, delimiter=';', lineterminator='\n'))
    arquivo.close()

    for i in planilha:
        if email in i:
            raise Duplicate
    cont=0
    for caracter in email:
        if caracter=="@":
            cont+=1
            if cont>1: raise NotLetter()
        if (not caracter.isalpha() and not caracter.isnumeric()) and caracter!="@" and caracter!="_" and caracter!=".":
            raise NotLetter()
        
def char_nome(Nome):
    for char in Nome:
        if not char.isalpha() and char!=" ":
            raise NotLetter()
        
def cadastrar_musicos():
    entrada_csv=[]
    Nome=input("Digite o nome do músico: ")
    try:
        char_nome(Nome)
    except NotLetter:
        print('Caracter inválido')

    entrada_csv.append(Nome.title())

    Email=input("Digite o email do músico: ")

    try:
        check_email(Email)
    except NotLetter:
        print('Caracter inválido')
    except Duplicate:
        print("Email já está cadastrado")

    entrada_csv.append(Email)

    Genero=(input("Digite o(s) gênero(s) musical(is):\n (Caso tenha mais de um separar por virgula sem espaço)\n ex: Rock,Funk"))
    genero_list=Genero.split(",")
    for i in range(len(genero_list)):
        genero_list[i]=genero_list[i].title()
    entrada_csv.append(genero_list)

    Instrumento=(input("Digite o(s) instrumento(s) musical(is):\n (Caso tenha mais de um separar por virgula sem espaço)\n ex: Flauta,Guitarra"))
    instrumento_list=Instrumento.split(",")
    for i in range(len(instrumento_list)):
        instrumento_list[i]=instrumento_list[i].title()
    entrada_csv.append(instrumento_list)
    
    with open('cadastro.csv','w+') as file:
        escrita=csv.DictWriter(file,skipinitialspace=True,delimiter=';', lineterminator='\n',fieldnames=["Nome", "Email", "Generos", "Instrumentos"])
        escrita.writeheader()
        escrita.writerows(entrada_csv)
        
class NotLetter(Exception):
    def __init__(self, message = 'Invalid Characters'):
        self.message = message
        super().__init__(self.message)
class Duplicate(Exception):
    def __init__(self, message = 'Duplicate Entrance'):
        self.message = message
        super().__init__(self.message)

def buscar_musicos():
    print("Para fazer uma busca escreva o nome da categoria seguido pelo valor procurado espaçado por ':'caso tenha mais de um valor de busca, separe por espaço\n Ex: Nome:Rafael,Gêneros:Rock")
    print("Selecione pelo menos uma categoria de 'Nome,Email,Gêneros,Instrumentos")
    busca=str(input())
    escolha_eou=int(input("Deseja os resultados batam com todas informações passadas(0) ou apenas uma(1)? "))
    dict_busca=dict(x.split(":") for x in busca.split(","))
    lista_busca=[]
    with open('cadastro.csv','r') as file:
        leitura=csv.DictReader(file,skipinitialspace=True,delimiter=';', lineterminator='\n')
        for l in leitura:
            try:
                for key, value in dict_busca.items():
                        filtro=list(filter(lambda x: x=="Gêneros" or x=="Instrumentos",key))
                        if key=="Gêneros" or key=="Instrumentos":                 
                            if value in l[key]:
                                lista_busca.append(l)
                                break
                        elif l[key]==value:
                            lista_busca.append(l)
                            break
            except:
                print("Categorias incorretas. Por favor, tente novamente.")
                break
    if escolha_eou==1:
        return lista_busca
    
    elif escolha_eou==0:
        proximo=False
        lista_busca2=[]
        for k in lista_busca:
            for key,value in dict_busca.items():
                if key=="Gêneros" or key=="Instrumentos":                 
                    if value not in k[key]:
                        proximo=True
                        break
                elif k[key]!=value:
                    proximo=True
                    break
            if proximo:
                proximo=False
            else:
                lista_busca2.append(k)
            
        return lista_busca2

def modificar_musicos():
    nova_busca=input("Digite o e-mail do Músico para alterar os dados cadastrais: ")

    with open('cadastro.csv','r') as file:
        leitura= csv.DictReader(file,skipinitialspace=True,delimiter=';', lineterminator='\n')
        lista_modifica=[]
        header=leitura.fieldnames

        for k in leitura:
            lista_modifica.append(k)

        flag_email=False

        for l in lista_modifica:

            if l["Email"]==nova_busca:
                
                flag_email=True
                print("Valores cadastrados:\n",l)
                alteracoes=input("Digite os novos valores seguindo o formato Gêneros:Rock,Folk;Instrumentos:Guitarra,Baixo")
                dict_altera=dict((x.split(":")) for x in alteracoes.split(";"))

                for keys,values in dict_altera.items():
                    dict_altera[keys]=values.split(",")
                    lista_modifica[lista_modifica.index(l)][keys]=dict_altera[keys]

        if not flag_email:
            print("Músico não encontrado, tente novamente")

    with open('cadastro.csv','w') as file2:
        escrita=csv.DictWriter(file2,skipinitialspace=True,delimiter=';', lineterminator='\n',fieldnames=header)
        escrita.writeheader()
        escrita.writerows(lista_modifica)

def combs(lista_combs,n):
    if n == 0:
        return [[]]
    saida=[]
    for j in range(len(lista_combs)):
        for i in combs(lista_combs[j+1:],n-1):
            saida.append([lista_combs[j],*i])
    return saida

def combinacao(lista_combs:list,n:int) ->list:
    '''
        Recebe uma lista_combs 1D que contenha todos os possíveis músicos e o instrumento que toca,
        recebe também uma variável n indicando a quantidade de integrantes da banda
        retorna um vetor contendo as possíveis combinações
    '''
    receba=combs(lista_combs,n)
    lista_final=[]
    for k in receba:
        lista_repetidos=[]
        lista_repetidos2=[]
        repetido=False
        for j in k:
            if j[1] in lista_repetidos or j[0] in lista_repetidos2: 
                ###verifica se tem o nome repetido j[0] na nova combinação ou se tem o instrumento repetido j[1]
                repetido=True
                break
            lista_repetidos.append(j[1])
            lista_repetidos2.append(j[0])
        if repetido==False:
            lista_final.append(k)
    return lista_final

def montar_bandas(dados):
    entrada_genero=input('Digite o Gênero desejado: ').title()
    entrada_qtde=int(input('Digite a quantidae de integrantes: '))
    entrada_instrumento=[]
    for _ in range(entrada_qtde):
        entrada_instrumento.append(input(f"Digite o instrumento do {_+1}º músico: ").title())
        possibilidades=[]
        for l in leitura:
            if entrada_genero in l["Gêneros"]:
                for i in range(len(entrada_instrumento)):
                    if entrada_instrumento[i] in l["Instrumentos"]:
                        possibilidades.append([l["Email"],entrada_instrumento[i]])

    possi_result=combinacao(possibilidades,entrada_qtde)
    for x in possi_result:
        print(' + '.join(str(e) for e in x))

def Menu():
    Entrada=int(input(" O que deseja fazer?\n 1-Cadastrar músicos\n 2-Buscar músicos\n 3-Modificar músicos\n 4-Montar bandas\n 5-Sair"))
    while Entrada in [1,7]:
        if Entrada==1:
            cadastrar_musicos()
        elif Entrada==2:
            buscar_musicos()  
        elif Entrada==3:
            modificar_musicos()
        elif Entrada==4:
            montar_bandas()
        elif Entrada==5:
            break
        else:
            print("Valor inválido, por favor tente novamente")
            print("Saída com sucesso")
            
arquivo()    
Menu()