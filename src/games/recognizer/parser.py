#coding:utf8
from PIL import Image, ImageEnhance
import numpy as np
from pytesser import image_to_string

class AbstractParser():
    def __init__(self, file_path):
        self.file_path = file_path
    def parse(self):
        pass

class PytesserParser(AbstractParser):
    # 直接识别图片
    def parse(self):
        image = Image.open(self.file_path)
        image = image.resize((100,100),Image.BOX)
        image = image.convert("L")
        enhancer = ImageEnhance.Contrast(image)
        image_enhancer = enhancer.enhance(4)
        return image_to_string(image)

class KnnParser(AbstractParser):
    def parse(self):
        pass
    # 图片转向量
    def image_to_vector(self):
        image = Image.open(self.file_path)
        image = image.resize((100,100),Image.BOX)
        image = image.convert("L")
        data = image.getdata(0)
        vector = np.array(data, dtype='float') / 255.0
        return vector
    # 图片转矩阵，传入：图片对象，返回：矩阵
    def image_to_matrix(file_path):
        image = Image.open(file_path)
        width, height = image.size
        image = image.convert("L")
        data = image.getdata(0)
        data = np.matrix(data, dtype='float') / 255.0
        matrix = np.reshape(data, (width, height))
        return matrix
    # 矩阵转图片，传入：矩阵，返回：图片对象
    def matrix_to_image(matrix):
        matrix = matrix * 255.0
        image = Image.fromarray(matrix.astype(np.uint8))
        return image


if __name__ == '__main__':
    if __name__ == '__main__':
        parser = PytesserParser(u"w:\\yay.jpg")
        result = parser.parse()
        print result

    # knn_parser = KnnParser(u"w:\\yay.jpg")
    # vector = knn_parser.image_to_vector()
    # print vector[0:10]