import random
def rolar_dados(quantidade):
    return [random.randint(1, 6) for _ in range(quantidade)]
