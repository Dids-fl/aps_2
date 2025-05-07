import random
def rolar_dados(quantidade):
    return [random.randint(1, 6) for _ in range(quantidade)]

def guardar_dado(dados_rolados,dados_no_estoque,dado_para_guardar):
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    del dados_rolados[dado_para_guardar]
    lista = [dados_rolados,dados_no_estoque]
    return lista

def remover_dado (dados_rolados,dados_no_estoque,dado_removido):
    dados_rolados.append(dados_no_estoque[dado_removido])
    del dados_no_estoque[dado_removido]
    lista = [dados_rolados,dados_no_estoque]
    return (lista)

def calcula_pontos_regra_simples(face_dos_dados):
    dvalores={}
    v1=0
    v2=0
    v3=0
    v4=0
    v5=0
    v6=0
    for n in face_dos_dados:
        if n == 1:
            v1= v1 + 1
        if n == 2:
            v2+= 2
        if n == 3:
            v3+=3
        if n == 4:
            v4+=4
        if n == 5:
            v5+=5
        if n ==6:
            v6+=6
    dvalores[1]=v1
    dvalores[2]=v2
    dvalores[3]=v3
    dvalores[4]=v4
    dvalores[5]=v5
    dvalores[6]=v6
    return dvalores

def calcula_pontos_soma(dados_rolados):
    total= 0
    for valor in dados_rolados:
        total += valor
    return total

def calcula_pontos_sequencia_baixa(lista):
    lista_ordenada = sorted(set(lista))
    soma = 0
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i] == lista_ordenada[i+1] - 1:
            soma += 1 
            if soma == 3:
                return 15
        else:
            soma = 0
    return 0
    
def calcula_pontos_sequencia_alta(lista):
    lista_ordenada = sorted(set(lista))
    soma = 0
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i] == lista_ordenada[i+1] - 1:
            soma += 1 
            if soma == 4:
                return 30
        else:
            soma = 0
    return 0

def calcula_pontos_full_house(lista):
    contar1 = lista.count(1)
    contar2 = lista.count(2)
    contar3 = lista.count(3)
    contar4 = lista.count(4)
    contar5 = lista.count(5)
    contar6 = lista.count(6)
    
    contagens = [contar1, contar2, contar3, contar4, contar5, contar6]

    soma = 0

    if 2 in contagens and 3 in contagens:
        for i in lista:
            soma = soma + i
        return soma
    else:
        return 0

def calcula_pontos_quadra (lista):
    contar1 = lista.count(1)
    contar2 = lista.count(2)
    contar3 = lista.count(3)
    contar4 = lista.count(4)
    contar5 = lista.count(5)
    contar6 = lista.count(6)
    
    contagens = [contar1, contar2, contar3, contar4, contar5, contar6]

    contar_maior = 0
    for i in contagens:
        if i > contar_maior:
            contar_maior=i

    soma = 0

    if contar_maior>3:
        for i in lista:
            soma = soma + i
        return soma
    else:
        return 0

