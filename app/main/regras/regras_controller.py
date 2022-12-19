from flask_restplus import Resource, Namespace
from app.main.regras.regras import regras, regras_duplasena, regras_lotofacil, regras_lotomania, regras_megasena, regras_quina

api = Namespace('Regras', description='Regras para geração de jogos')


@api.route('/all')
class RegrasAleatorioController(Resource):
    @api.response(200, "Documento De Regras gerado com sucesso!")
    def get(self):
        return regras(), 200


@api.route('/duplasena')
class RegrasDuplasenaController(Resource):
    @api.response(200, "Documento De Regras gerado com sucesso!")
    def get(self):
        return regras_duplasena(), 200


@api.route('/lotofacil')
class RegrasLotofacilController(Resource):
    @api.response(200, "Documento De Regras gerado com sucesso!")
    def get(self):
        return regras_lotofacil(), 200


@api.route('/lotomania')
class RegrasLotomaniaController(Resource):
    @api.response(200, "Documento De Regras gerado com sucesso!")
    def get(self):
        return regras_lotomania(), 200


@api.route('/megasena')
class RegrasMegasenaController(Resource):
    @api.response(200, "Documento De Regras gerado com sucesso!")
    def get(self):
        return regras_megasena(), 200


@api.route('/quina')
class RegrasQuinaController(Resource):
    @api.response(200, "Documento De Regras gerado com sucesso!")
    def get(self):
        return regras_quina(), 200
