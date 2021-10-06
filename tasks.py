from flask import Flask, request
from flask_restful import Resource, Api

import json

app = Flask(__name__)
api = Api(app)

tasks = []

class Tasks(Resource):
    def get(self):
        return tasks

    def post(self):
        newTask = json.loads(request.data)
        tasks.append(newTask)
        return {
            "message": "New Task Created!",
            "Task": newTask
        }

class Task(Resource):
    def get(self, indice):
        try:
            return tasks[indice]
        except IndexError:
            message = "Indice Task Not Found"
            return {
                "message": message,
                "status": "Error!"
            }
        except:
            message = "Indice Task Not Found"
            return {
                "message": message,
                "status": "Unknow Error!"
            }

    def delete(self, indice):
        tasks.pop(indice)
        return {
            "message": "Removido!",
            "Atual": tasks
        }

api.add_resource(Tasks, '/tasks/')
api.add_resource(Task, '/tasks/<int:indice>')

if __name__ == '__main__':
    app.run(debug=True)