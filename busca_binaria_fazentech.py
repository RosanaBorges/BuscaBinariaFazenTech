def busca_binaria(id_animal, minimo, maximo, buscar):
    
    if maximo < minimo:
        return -1

    meio= (minimo + maximo) //2
    if id_animal[meio] == buscar:
        return meio

    elif id_animal [meio] > buscar:
        return busca_binaria (id_animal, minimo, meio -1, buscar)
    else:
        return busca_binaria (id_animal, meio +1, maximo, buscar)

id_animal=[2,4,6,8,10,12,14,16,18,20]
nome_animal=['mimosa','caninha','oracia','alberta','boneca','cidinha','alma','ceu','vidinha','nina']

codigo =  input ('Digite o ID do animal para fezer a pesquisa:')
id_procurado = int (codigo)
busca_binaria(id_animal, 0, len(id_animal) -1, id_procurado)

para_teste = busca_binaria(id_animal, 0, len(id_animal) -1, id_procurado)
if(int(para_teste)!=-1):
    print('Os dados do animal solicitado são:', nome_animal[int(para_teste)])
else:
    print('Id do animal não identificado')
