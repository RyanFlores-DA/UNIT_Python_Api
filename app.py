from flask import Flask
from flask_restful import Resource, Api
from models import Pessoas

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, id):
        try:
            pessoa = Pessoas.query.filter_by(id=id).first()
            response = {
                'nome': pessoa.nome,
                'id': pessoa.id
            }
            return response
        except:
            return {
                'erro': 'Algo deu errado!'
            }
class Usuarios(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        return pessoas


api.add_resource(Pessoa, '/pessoas/<int:id>')
api.add_resource(Usuarios, '/pessoas')

if __name__ == '__main__':
    app.run(debug=True)