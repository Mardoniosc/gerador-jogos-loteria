from flask_restplus import Resource, Namespace
from flask import request
from app.main.megasena.megasena import megasena_aleatorio, megasena_duque, fechamento

api = Namespace('Megasena', description='Gerenciador de jogos megasena')


@api.route('/aleatorio')
class MegasenaAleatorioController(Resource):
    @api.response(200, "JOGO GERADO COM SUCESSO")
    def get(self):
        return megasena_aleatorio(), 200


@api.route('/duque')
class MegasenaDuqueController(Resource):
    @api.response(200, "JOGO GERADO COM SUCESSO")
    def get(self):
        return megasena_duque(), 200


argumentos = api.parser()
argumentos.add_argument('total_numeros_fechamento', choices=[12,20], default=12, required=True)
argumentos.add_argument('para_acertar', choices=[
                        4, 5, 6], default=4, required=True)
argumentos.add_argument('geracao_numeros', choices=[
                        'ALEATORIO', 'DUQUE', 'ESCOLHER_NUMEROS'], required=True, dest='Tipos de números para fechamento', default='ALEATORIO')
argumentos.add_argument('numeros_fechamento', type=str,
                        dest='Informar os numeros separados por virgula', default='0,1,2')


@api.route('/fechamento')
class MegasenaFechamentoController(Resource):
    @api.response(200, "JOGO GERADO COM SUCESSO")
    @api.expect(argumentos)
    def get(self):
        jogo = fechamento(request.args)
        return jogo, 200
