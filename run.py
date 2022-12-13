# coding: utf-8

"""
    .NOTES
    ===========================================================================
    Created with:   VSCode Classic v1.73.0
    Created on:   	12/12/2022
    Created by:   	Mardonio Silva da Costa
    Sistema:       	Sistema Gerador de Jogos de loteria
    version:        1.0.0
    ===========================================================================
    .DESCRIPTION
      Responsavel pela Geração de jogos da loteria
    .UPDATES
      00/00/2022 - Mardonio - 
"""

from app import app

if __name__ == '__main__':
    app.run(port=5000, debug=True)

def create_app():
  return app