from PIL import Image
import numpy as np


def image_to_matrix(file_path):
    image = Image.open(file_path)
    width,height = image.size
    # image = image.convert("L")
    print width,"  ",height
    data = image.getdata(0)
    print len(list(data))
    print list(data)
    data = np.matrix(data, dtype='float')/255.0
    newdata = np.reshape(data,(width,height))
    return newdata


if __name__ == '__main__':
    image_to_matrix(u"z:\\yay.jpg")
