from flask import Flask, Blueprint, url_for
from flask_restplus import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from app.main.duplasena.duplasena_controller import api as duplasena_ns
from app.main.lotofacil.lotofacil_controller import api as lotofacil_ns
from app.main.lotomania.lotomania_controller import api as lotomania_ns
from app.main.megasena.megasena_controller import api as megasena_ns
from app.main.quina.quina_controller import api as quina_ns

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)

authorizations = {
    'bearer': {
        'name': "Authorization",
        'in': "header",
        'type': "apiKey",
        'description': "Insert your JWT Token here!"
    }
}

class PatchedApi(Api):
    @property
    def specs_url(self):
        return url_for(self.endpoint('specs'), _external=False)

api = PatchedApi(app, 
    title='Api Geradora de jogos de loteria', 
    version='1.0.0', 
    description='Api feita para padronização de geração de jogos',
    prefix='/api', 
    authorizations=authorizations)

api.add_namespace(duplasena_ns, path='/duplasena')
api.add_namespace(lotofacil_ns, path='/lotofacil')
api.add_namespace(lotomania_ns, path='/lotomania')
api.add_namespace(megasena_ns, path='/megasena')
api.add_namespace(quina_ns, path='/quina')