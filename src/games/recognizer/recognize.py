# coding=utf8
import json
import os

from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename

from config import configs
from src.games.recognizer.image_parser import KnnParser


class Recognizer(Resource):
    # 上传图片并识别
    def post(self):
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(configs.get("upload_dir"), filename)
            file.save(file_path)
        else:
            return json.dumps({"message": "illegal filename or empty file!"})
        parser = KnnParser()
        result = parser.parse(file_path)
        return json.dumps({'result': result})


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in configs.get("allowed_extensions")
