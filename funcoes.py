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

