from flask_restful import Resource
import random

class Recognizer(Resource):
    def put(self):
        result = random.random()
        return {'result': result}