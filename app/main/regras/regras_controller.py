from flask_restplus import Resource, Namespace
from app.main.regras.regras import regras_aleatorio

api = Namespace('Regras', description='Regras para geração de jogos')

@api.route('/all')
class RegrasAleatorioController(Resource):
  @api.response(200, "Documento De Regras gerado com sucesso!")
  def get(self):
      return regras_aleatorio(), 200