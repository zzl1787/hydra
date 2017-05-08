from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from src.games.recognizer.recognizer import Recognizer
from src.user.user import User

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Recognizer,'/games/recognizer')
api.add_resource(User,'/users')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
