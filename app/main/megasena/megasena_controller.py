from flask_restplus import Resource, Namespace
from app.main.megasena.megasena import megasena_aleatorio, megasena_duque

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