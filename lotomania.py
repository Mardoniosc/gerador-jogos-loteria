# coding: utf-8

"""
    .NOTES
    ===========================================================================
    Created with:   VSCode Classic v1.73.0
    Created on:   	12/12/2022
    Created by:   	Mardonio Silva da Costa
    Filename:     	lotomania.py
    ===========================================================================
    .DESCRIPTION
      Responsavel pela criação de jogos da lotomania
    .UPDATES
      00/00/2022 - Mardonio - 
"""

from random import sample

def lotomania_aleatorio():
  numeros = list(range(0, 100))
  jogo =  sample(numeros, 50)
  jogo = { 'Jogo' : sorted(jogo)}
  return jogo