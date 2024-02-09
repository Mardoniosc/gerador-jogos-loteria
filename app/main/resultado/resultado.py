from random import sample
import requests

API_URL = 'https://loteriascaixa-api.herokuapp.com/api'


def getResultado(loteria, concurso):
    response_API = requests.get(API_URL + '/' + loteria + '/' + concurso)
    response = response_API.json()
    # resultado = response['dezenas']
    # resultado = list(map(int, resultado))
    # resultado_ordem = sorted(resultado)
    return response


def resultado(argumentos):
    concurso = argumentos.get('concurso')
    loteria = argumentos.get('loteria')

    if(concurso == '0'):
        concurso = 'latest'

    numeros = list(map(int, argumentos.get('numeros_jogados').split(",")))

    resultado = getResultado(loteria, concurso)
    dezenas_sorteadas = list(map(int, resultado['dezenas']))

    # CONTA QUANTIDADE DE ACERTOS
    acertos_ = set(dezenas_sorteadas).intersection(numeros)
    acertos = len(acertos_)
    numeros_acertos = str(acertos_).replace('{', '').replace('}', '')

    print(resultado)

    response = {
        'Data Sorteio' : resultado['data'],
        'concurso' : resultado['concurso'],
        'Quantidade de Acertos': acertos,
        'Números acertos': numeros_acertos,
        'Dezenas Sorteadas': dezenas_sorteadas,
        'premiacoes': resultado['premiacoes']
    }

    return response
