# coding: utf-8

"""
    .NOTES
    ===========================================================================
    Created with:   VSCode Classic v1.73.0
    Created on:   	12/12/2022
    Created by:   	Mardonio Silva da Costa
    Filename:     	duplasena.py
    ===========================================================================
    .DESCRIPTION
      Responsavel pela criação de jogos da duplasena
    .UPDATES
      00/00/2022 - Mardonio - 
"""

from random import sample

def duplasena_aleatorio():
  numeros = list(range(1, 61))
  jogo1 =  sample(numeros, 6)
  jogo2 =  sample(numeros, 6)
  jogo = { 'Jogos' : [sorted(jogo1), sorted(jogo2)]}
  return jogo