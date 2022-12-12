# coding: utf-8

"""
    .NOTES
    ===========================================================================
    Created with:   VSCode Classic v1.73.0
    Created on:   	12/12/2022
    Created by:   	Mardonio Silva da Costa
    Filename:     	lotofacil.py
    ===========================================================================
    .DESCRIPTION
      Responsavel pela criação de jogos da lotofacil
    .UPDATES
      00/00/2022 - Mardonio - 
"""

from random import sample
import requests 

API_URL = 'https://api-loteria.servicosmsc.com.br/api/lotofacil/latest'

# GERA O JOGO SEM NENHUM TIPO DE REGRA
def lotofacil_aleatorio():
  numeros = list(range(1, 26))
  jogo =  sample(numeros, 15)
  jogo = { 'Jogo' : sorted(jogo)}
  return jogo

def lotofacil_base_ultimo():
  lotofacil = list(range(1, 26))
  response_API = requests.get(API_URL)
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