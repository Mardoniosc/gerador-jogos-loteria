from flask_restplus import Resource, Namespace
from app.main.quina.quina import quina_aleatorio

api = Namespace('Quina', description='Gerenciador de jogos quina')

@api.route('/aleatorio')
class QuinaAleatorioController(Resource):
  @api.response(200, "JOGO GERADO COM SUCESSO")
  def get(self):
      return quina_aleatorio(), 200