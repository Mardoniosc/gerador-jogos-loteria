# coding: utf-8

"""
    .NOTES
    ===========================================================================
    Created with:   VSCode Classic v1.73.0
    Created on:   	12/12/2022
    Created by:   	Mardonio Silva da Costa
    Filename:     	run.py
    ===========================================================================
    .DESCRIPTION
      Responsavel pela execução do projeto principal
    .UPDATES
      00/00/2022 - Mardonio - 
"""

from app import app

if __name__ == '__main__':
    app.run(port=5000, debug=True)

def create_app():
  return app