from random import sample

def quina_aleatorio():
  numeros = list(range(1, 81))
  jogo =  sample(numeros, 5)
  jogo = { 'Jogo' : sorted(jogo)}
  return jogo