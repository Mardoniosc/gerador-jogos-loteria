from flask_restplus import Resource, Namespace
from flask import request
from app.main.resultado.resultado import resultado

api = Namespace('Resultado', description='Gerenciador de jogos resultado')

argumentos = api.parser()
argumentos.add_argument('loteria', choices=[
                        'dupla-sena', 'lotofacil', 'lotomania', 'mega-sena', 'quina'], required=True, default='dupla-sena')
argumentos.add_argument(
    'concurso', type=int, dest='Informar os numeros separados por virgula', default='0', required=True)
argumentos.add_argument('numeros_jogados', type=str,
                        dest='Informar os numeros separados por virgula', default='1,2,3,4')

@api.route('/valida-resultado')
class ResultadoAleatorioController(Resource):
    @api.response(200, "Econtrado resultado")
    @api.expect(argumentos)
    def get(self):
        response = resultado(request.args)
        return response, 200
