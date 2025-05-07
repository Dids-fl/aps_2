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
