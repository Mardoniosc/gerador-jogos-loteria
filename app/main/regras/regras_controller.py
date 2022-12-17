from flask_restplus import Resource, Namespace
from app.main.regras.regras import getAllRoles

api = Namespace('Regras', description='Regras da geração de jogos')

@api.route('/all')
class RegrasAllController(Resource):
  @api.response(200, "Listado regras com sucesso")
  def get(self):
    return getAllRoles, 200