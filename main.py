from flask import Flask, json
from random import sample
import requests 
import os
from funcoes import jogo_mega_sena

app = Flask(__name__)

# CONSTANTES 
API_URL = 'https://api-loteria.servicosmsc.com.br/api/lotofacil/latest'

@app.route('/')
def home():
  response = app.response_class(
    response=json.dumps({'Sistema': 'Api de geração de jogos de loteria'}),
    status=200,
    mimetype='application/json'
  )

  return response

# JOGOS DA LOTOFACIL
@app.route('/lotofacil/aleatorio')
def jogo_aleatorio_lotofacil():

  lotofacil_numeros = list(range(1, 26))
  jogo =  sample(lotofacil_numeros, 15)
  jogo = sorted(jogo)

  response = app.response_class(
    response=json.dumps({ 'jogo': str(jogo) }),
    status=200,
    mimetype='application/json'
  )

  return response

@app.route('/lotofacil/base/ultimo')
def base_ultimo():
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

  todos_jogos = [str(sorted(jogo1)),str(sorted(jogo2)),str(sorted(jogo3)),str(sorted(jogo4)),str(sorted(jogo5)),str(sorted(jogo6))]

  json_response = {
    'concurso_base': response['concurso'],
    'jogos': todos_jogos
  }

  response = app.response_class(
    response=json.dumps(json_response),
    status=200,
    mimetype='application/json'
  )

  return response

# JOGOS MEGA SENA
@app.route('/mega-sena/aleatorio')
def jogo_aleatorio_mega():

  numeros = list(range(1, 61))
  jogo =  sample(numeros, 6)
  jogo = sorted(jogo)

  response = app.response_class(
    response=json.dumps({ 'jogo': str(jogo) }),
    status=200,
    mimetype='application/json'
  )

  return response

@app.route('/mega-sena/duque')
def jogo_duque_mega():
  jogo =  jogo_mega_sena()
  jogo = sorted(jogo)

  response = app.response_class(
    response=json.dumps({ 'jogo': str(jogo) }),
    status=200,
    mimetype='application/json'
  )

  return response


# PRODUCTION
def create_app():
  return app

# development
if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True, host='0.0.0.0', port=port)
