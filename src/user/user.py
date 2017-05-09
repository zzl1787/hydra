from flask_restful import Resource


class User(Resource):
    def get(self):
        return [{
            'name': 'zhaozhe',
            'email': 'zzl1787@gmail.com',
            'website': 'www.imzhaozhe.com'
        }]
