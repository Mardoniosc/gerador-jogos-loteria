from flask_restplus import Resource, Namespace
from app.main.lotomania.lotomania import lotomania_aleatorio

api = Namespace('Lotomania', description='Gerenciador de jogos lotomania')

@api.route('/aleatorio')
class LotomaniaAleatorioController(Resource):
  @api.response(200, "JOGO GERADO COM SUCESSO")
  def get(self):
      return lotomania_aleatorio(), 200