from flask_restplus import Resource, Namespace
from app.main.duplasena.duplasena import duplasena_aleatorio

api = Namespace('Duplasena', description='Gerenciador de jogos duplasena')

@api.route('/aleatorio')
class DuplasenaAleatorioController(Resource):
  @api.response(200, "JOGO GERADO COM SUCESSO")
  def get(self):
      return duplasena_aleatorio(), 200