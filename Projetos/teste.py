def combs(lista_combs,n):
    if n == 0:
        return [[]]
    saida=[]
    for j in range(len(lista_combs)):
        for i in combs(lista_combs[j+1:],n-1):
            saida.append([lista_combs[j],*i])
    return saida
    