from random import sample

def megasena_aleatorio():
  numeros = list(range(1, 61))
  jogo =  sample(numeros, 6)
  jogo = { 'Jogo' : sorted(jogo)}
  return jogo

def megasena_duque():
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
  jogo = { 'Jogo' : sorted(jogo_mega)}
  
  return jogo

def fechamento(item):
  tipo = item.get('geracao_numeros') 
  total = item.get('total_numeros_fechamento') 
  numeros = item.get('numeros_fechamento') 
  para_acertar = item.get('para_acertar') 
  
  if(tipo == 'ESCOLHER_NUMEROS'):
    numeros = list(map(int, numeros.split(",")))

    if(len(numeros) < int(total)):
      return {'Alerta': 'Números de fechamento informado é menor que ' + total}

  if(tipo == 'ALEATORIO'):
    numeros_sorteaod = list(range(1, 61))
    numeros =  sample(numeros_sorteaod, int(total))

  if(tipo == 'DUQUE'):
    numeros_baixos = [1,2,3,4,5,6,7,8,9]
    duque = [30,31,32,33,34,35,36,37,38,39]
    numeros_altos = [51,52,53,54,55,56,57,58,59,60]

    numeros_completos = [10,11,12,13,14,15,16,17,18,19,
                          20,21,22,23,24,25,26,27,28,29,
                          40,41,42,43,44,45,46,47,48,49,50]

    NB = sample(numeros_baixos, 1)
    DUQUE = sample(duque, 3)
    NA = sample(numeros_altos, 1)
    NC = sample(numeros_completos, int(total) - 5)
    numeros = (NB + DUQUE + NA + NC)

  jogos = []
  arquivoFechamento = 'app/assets/megasena/' + total + '-'+ para_acertar +'SE6.txt'

  with open(arquivoFechamento, 'r') as fd:
    for x in fd:
      jogoFechamento = []
      jogoIndex = list(map(int, x.split(",")))
      for i in jogoIndex:
        jogoFechamento.append(numeros[i])
      jogos.append(jogoFechamento)
    fd.close()
  
  return {'Jogos': jogos }