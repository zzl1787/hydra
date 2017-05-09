#coding=utf8
from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api
from werkzeug.utils import secure_filename

from src.games.recognizer.image_parser import KnnParser
from src.user.user import User
from src.config import configs
import json
import os

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(User,'/users')



#上传图片并识别
@app.route('/games/recognizer', methods=['POST'])
def speculateImage():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(configs.get("upload_dir"), filename))
        file_path = os.path.join(configs.get("upload_dir"), filename)
    else:
        return json.dumps({"message": "illegal filename or empty file!"})
    parser = KnnParser()
    result = parser.parse(file_path)
    return json.dumps({'result': result})
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in configs.get("allowed_extensions")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
