# coding: utf-8

"""
    .NOTES
    ===========================================================================
    Created with:   VSCode Classic v1.73.0
    Created on:   	12/12/2022
    Created by:   	Mardonio Silva da Costa
    Filename:     	app.py
    ===========================================================================
    .DESCRIPTION
      Responsavel pela rotas e resposta de chamada na REST API
    .UPDATES
      00/00/2022 - Mardonio - 
"""

from flask import Flask, jsonify

from lotofacil import lotofacil_aleatorio, lotofacil_base_ultimo, lotofacil_nao_sorteado
from megasena import mega_aleatorio, mega_duque
from duplasena import duplasena_aleatorio
from lotomania import lotomania_aleatorio
from quina import quina_aleatorio

app = Flask(__name__)

@app.route('/')
def status_api():
  response = {'status': 'ok'}
  return jsonify(response), 200

# JOGOS DA LOTOFACIL
@app.route('/lotofacil/aleatorio')
def aleatorio_lotofacil():
  response = lotofacil_aleatorio()
  return jsonify(response), 200

@app.route('/lotofacil/base/ultimo')
def base_ultimo():
  response = lotofacil_base_ultimo()
  return jsonify(response), 200

@app.route('/lotofacil/nao-sorteado')
def nao_sorteado():
  response = lotofacil_nao_sorteado()
  return jsonify(response), 200

# JOGOS MEGA SENA
@app.route('/mega-sena/aleatorio')
def jogo_aleatorio_mega():
  response = mega_aleatorio()
  return jsonify(response), 200

@app.route('/mega-sena/duque')
def jogo_duque_mega():
  response = mega_duque()
  return jsonify(response), 200

# JOGOS quina
@app.route('/quina/aleatorio')
def jogo_aleatorio_quina():
  response = quina_aleatorio()
  return jsonify(response), 200

# JOGOS duplasena
@app.route('/duplasena/aleatorio')
def jogo_aleatorio_duplasena():
  response = duplasena_aleatorio()
  return jsonify(response), 200

# JOGOS lotomania
@app.route('/lotomania/aleatorio')
def jogo_aleatorio_lotomania():
  response = lotomania_aleatorio()
  return jsonify(response), 200