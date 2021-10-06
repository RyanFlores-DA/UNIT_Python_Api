from flask_restful import Resource

skills = [
    'Java',
    'Python',
    'NodeJS',
    'PHP',
    'MongoDB',
    'Lua',
    'Go'
]

class Skills(Resource):
    def get(self):
        return skills