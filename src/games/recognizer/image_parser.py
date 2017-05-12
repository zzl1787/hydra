# coding:utf8
import functools
import os

from PIL import Image, ImageEnhance
from pandas import DataFrame
from pytesser import image_to_string

from config import configs
from src.utils.distance import *


class AbstractParser():
    def __init__(self):
        pass

    def parse(self):
        pass


# 图片预处理装饰器
def preHandle(func):
    @functools.wraps(func)
    def decorator(image):
        image = image.resize((300, 370), Image.BOX)
        image = image.convert("L")
        ret = func(image)
        return ret

    return decorator


# 加载训练图片dataframe
def load_dataset():
    sample_dir = configs.get("recognizer_sample_dir")
    files = os.listdir(sample_dir)
    dataset = np.mat([])
    index = []
    for file in files:
        image = Image.open(os.path.join(sample_dir, file))
        row = image_to_vector(image)
        index.append(file.replace(".png", ""))
        if (dataset.size == 0):
            dataset = np.mat(row)
        else:
            dataset = np.row_stack((dataset, row))
    dataframe = DataFrame(dataset, index)
    return dataframe


# 图片转矩阵，传入：图片对象，返回：矩阵
def image_to_matrix(image):
    width, height = image.size
    image = image.resize((300, 370), Image.BOX)
    image = image.convert("L")
    data = image.getdata(0)
    data = np.matrix(data, dtype='float') / 255.0
    matrix = np.reshape(data, (width, height))
    return DataFrame(matrix)


# 矩阵转图片，传入：矩阵，返回：图片对象
def matrix_to_image(matrix):
    matrix = matrix * 255.0
    image = Image.fromarray(matrix.astype(np.uint8))
    return image


# 图片转向量
def image_to_vector(image):
    image = image.resize((300, 370), Image.BOX)
    image = image.convert("L")
    data = image.getdata(0)
    vector = np.array(data, dtype='float') / 255.0
    return vector


class PytesserParser(AbstractParser):
    # 直接识别图片
    def parse(self, image):
        image = image.resize((300, 370), Image.BOX)
        image = image.convert("L")
        enhancer = ImageEnhance.Contrast(image)
        image_enhancer = enhancer.enhance(4)
        return image_to_string(image_enhancer)


class KnnParser(AbstractParser):
    def parse(self, image):
        vector = image_to_vector(image)
        dataframe = load_dataset()
        distances = {}
        for index, row in dataframe.iterrows():
            distances[index] = eucldist(vector, row)
        result = min(distances.items(), key=lambda x: x[1])[0]
        return result

if __name__ == '__main__':
    parser = KnnParser()
    result = parser.parse(Image.open('w:\\1.png'))
    print result