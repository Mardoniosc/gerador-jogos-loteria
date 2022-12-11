from random import sample

def jogo_mega_sena():
    numeros_baixos = [1,2,3,4,5,6,7,8,9]
    duque = [30,31,32,33,34,35,36,37,38,39]
    numeros_altos = [51,52,53,54,55,56,57,58,59,60]

    numeros_completos = [10,11,12,13,14,15,16,17,18,19,
                         20,21,22,23,24,25,26,27,28,29,
                         40,41,42,43,44,45,46,47,48,49,50]

    NB = sample(numeros_baixos, 1)
    DUQUE = sample(duque, 2)
    NA = sample(numeros_altos, 1)
    NC = sample(numeros_completos, 2)
    jogo_mega = (NB + DUQUE + NA + NC)
    jogo_mega = sorted(jogo_mega)

    return jogo_mega