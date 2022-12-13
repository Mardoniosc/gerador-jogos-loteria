from random import sample
import requests 
from app.utils.auxFunc import resultado_lista_inteiro, compara_resultado, valida_sequencia

API_URL = 'https://api-loteria.servicosmsc.com.br/api/lotofacil'

# GERA O JOGO SEM NENHUM TIPO DE REGRA
def lotofacil_aleatorio():
  numeros = list(range(1, 26))
  jogo =  sample(numeros, 15)
  jogo = { 'Jogo' : sorted(jogo)}
  return jogo

# GERAR JOGO COM BASE NO ULTIMO RESULTADO
def lotofacil_base_ultimo():
  lotofacil = list(range(1, 26))
  response_API = requests.get(API_URL + '/latest')
  response = response_API.json()
  ultimo_resultado = response['dezenas']
  ultimo_resultado = list(map(int, ultimo_resultado))
  ultimo_resultado_ordem = sorted(ultimo_resultado)
  nao_sorteados = list(set(lotofacil) - set(ultimo_resultado))

  # REALIZANDO REGRAS PARA SORTEAR NOVOS NUMEROS
  A = (nao_sorteados[0:2] + ultimo_resultado_ordem[0:3])
  B = (nao_sorteados[2:4] + ultimo_resultado_ordem[3:6])
  C = (nao_sorteados[4:6] + ultimo_resultado_ordem[6:9])
  D = (nao_sorteados[6:8] + ultimo_resultado_ordem[9:12])
  E = (nao_sorteados[8:10] + ultimo_resultado_ordem[12:15])

  jogo1 = A + B + C
  jogo2 = A + B + D
  jogo3 = A + B + E
  jogo4 = A + C + D
  jogo5 = A + C + E
  jogo6 = A + D + E

  todos_jogos = [sorted(jogo1),sorted(jogo2),sorted(jogo3),sorted(jogo4),sorted(jogo5),sorted(jogo6)]

  json_response = {
    'concurso_base': response['concurso'],
    'jogos': todos_jogos
  }

  return json_response

def lotofacil_nao_sorteado():
  response_API = requests.get(API_URL)
  response = response_API.json()

  pode_jogar = True
  while(pode_jogar):
    jogo = lotofacil_aleatorio()
    jogo = jogo['Jogo']
    for resultado in response:
      resultado_lista = resultado_lista_inteiro(resultado['dezenas'])
      jogo2 = resultado_lista_inteiro(resultado_lista)
      if(valida_sequencia(jogo) == False):
        if (compara_resultado(jogo, jogo2) != 15):
          pode_jogar = False
          return { 'Jogo' : sorted(jogo)}