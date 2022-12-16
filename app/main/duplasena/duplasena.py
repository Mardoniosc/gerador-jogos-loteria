from random import sample


def duplasena_aleatorio():
    numeros = list(range(1, 51))
    jogo = sample(numeros, 6)
    jogo = {'Jogo': sorted(jogo)}
    return jogo
