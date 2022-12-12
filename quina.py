# coding: utf-8

"""
    .NOTES
    ===========================================================================
    Created with:   VSCode Classic v1.73.0
    Created on:   	12/12/2022
    Created by:   	Mardonio Silva da Costa
    Filename:     	quina.py
    ===========================================================================
    .DESCRIPTION
      Responsavel pela criação de jogos da quina
    .UPDATES
      00/00/2022 - Mardonio - 
"""

from random import sample

def quina_aleatorio():
  numeros = list(range(1, 81))
  jogo =  sample(numeros, 5)
  jogo = { 'Jogo' : sorted(jogo)}
  return jogo