from random import sample

def lotomania_aleatorio():
  numeros = list(range(0, 100))
  jogo =  sample(numeros, 50)
  jogo = { 'Jogo' : sorted(jogo)}
  return jogo