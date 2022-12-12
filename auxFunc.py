# coding: utf-8

"""
    .NOTES
    ===========================================================================
    Created with:   VSCode Classic v1.73.0
    Created on:   	12/12/2022
    Created by:   	Mardonio Silva da Costa
    Filename:     	auxFunc.py
    ===========================================================================
    .DESCRIPTION
      Funções auxiliares na criação/validação de jogos
    .UPDATES
      00/00/2022 - Mardonio - 
"""
def resultado_lista_inteiro(jogo):
    jogo = list(map(int, jogo))
    return jogo

def compara_resultado(jogo1, jogo2):
    resultado = set(jogo1).intersection(jogo2)
    acertos = len(resultado)
    return acertos

# valida se na lista exite 5 numeros em sequencia
def valida_sequencia(lista_int):
  for i, v in enumerate(lista_int[:-4]):  
    if (lista_int[i:i+5]) == [*range(v, v+5)]:     
      return True
  
  return False