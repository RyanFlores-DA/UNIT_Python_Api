from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {
        "name": "juni",
        "skills": [
            "python",
            "javascript"
        ]
    },
    {
        "name": "jarbas",
        "skills": [
            "c#",
            "java"
        ]
    }
]
# Operações realizadas com get e post
@app.route('/devs', methods=['GET', 'POST'])
def devs():
    if request.method == "GET":
        return jsonify(developers)
    elif request.method == "POST":
        newDev = json.loads(request.data)
        developers.append(newDev)
        return jsonify({
            "message": "Created!",
            "newValue":newDev
        })
# OPERAÇÕES COM UM ÚNICO DEV IDENTIFICADO PELO INDICE DELE
@app.route('/devs/<int:indice>', methods=['GET', 'PUT', 'DELETE'])
def dev(indice):
    try:
        developers[indice]
    except IndexError:
        message = "Developer ID {} not found!".format(indice)
        return jsonify({
            "mensage": message,
            "status": "Error!"
        })
    except:
        message = "Deu um erro desconhecido!"
        return jsonify({
            "mensage": message,
            "status": "Error!"
        })
    # Verifica se o método da requisição é GET
    if request.method == "GET":
        return developers[indice]
    # Verifica se o método da requisição é PUT
    elif request.method == "PUT":
        newValue = json.loads(request.data)
        developers[indice] = newValue
        return jsonify({
            "message": "Updated!",
            "newValue": newValue
        })
    # Verifica se o método da requisição é DELETE
    elif request.method == "DELETE":
        developers.pop(indice)
        return jsonify({
            "message": "Removido!",
            "Array atual": developers
        })

if __name__ == '__main__':
    app.run(debug=True)
