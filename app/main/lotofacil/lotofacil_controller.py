from flask_restplus import Resource, Namespace
from app.main.lotofacil.lotofacil import lotofacil_aleatorio, lotofacil_base_ultimo, lotofacil_nao_sorteado

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