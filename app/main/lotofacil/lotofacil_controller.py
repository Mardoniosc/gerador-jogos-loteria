from flask_restplus import Resource, Namespace
from flask import request
from app.main.lotofacil.lotofacil import lotofacil_aleatorio, lotofacil_base_ultimo, lotofacil_nao_sorteado, fechamento

api = Namespace('Lotofacil', description='Gerenciador de jogos lotofacil')

@api.route('/aleatorio')
class LotofacilAleatorioController(Resource):
  @api.response(200, "JOGO GERADO COM SUCESSO")
  def get(self):
      return lotofacil_aleatorio(), 200

@api.route('/nao-sorteado')
class LotofacilNaoSorteadoController(Resource):
  @api.response(200, "JOGO GERADO COM SUCESSO")
  def get(self):
      return lotofacil_nao_sorteado(), 200

@api.route('/base-ultimo')
class LotofacilUltimoController(Resource):
  @api.response(200, "JOGO GERADO COM SUCESSO")
  def get(self):
      return lotofacil_base_ultimo(), 200

argumentos = api.parser()
argumentos.add_argument('total_numeros_fechamento', choices=[16,17,18,19,20,21,22], default=20, required=True)
argumentos.add_argument('para_acertar', choices=[11,12,13,14,15], default=14, required=True)
argumentos.add_argument('acertando', choices=[14,15], default=15, required=True, dest='Se acertar esse total dentro do numero total de fechamento')
argumentos.add_argument('geracao_numeros', choices=['ALEATORIO', 'ESCOLHER_NUMEROS'], required=True, dest='Tipos de números para fechamento', default='ALEATORIO')
argumentos.add_argument('numeros_fechamento', type=str, dest='Informar os numeros separados por virgula', default='1,2,3')

@api.route('/fechamento')
class MegasenaFechamentoController(Resource):
    @api.response(200, "JOGO GERADO COM SUCESSO")
    @api.expect(argumentos)
    def get(self):
        jogo = fechamento(request.args)
        return jogo, 200