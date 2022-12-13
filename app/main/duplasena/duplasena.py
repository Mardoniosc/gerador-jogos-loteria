from random import sample

def duplasena_aleatorio():
  numeros = list(range(1, 61))
  jogo1 =  sample(numeros, 6)
  jogo2 =  sample(numeros, 6)
  jogo = { 'Jogos' : [sorted(jogo1), sorted(jogo2)]}
  return jogo