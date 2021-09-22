from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/user')
def user():
    return "Nome do usuario"

if __name__ == '__main__':
    app.run(debug=True)