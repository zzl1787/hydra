# coding=utf8
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from src.user.user import User
from src.games.recognizer.recognize import Recognizer

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(User, '/users')
api.add_resource(Recognizer, '/games/recognizer')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
