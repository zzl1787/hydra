from PIL import Image
import numpy as np


def image_to_string(file_path):
    image = Image.open(file_path)
    # image.show()
    width,height = image.size
    # image = image.convert("L")
    # image.show()
    data = image.getdata()
    # data = np.matrix(data, dtype='float')/255.0
    # newdata = np.reshape(data,(width,height))
    # print newdata
    return


if __name__ == '__main__':
    image_to_string(u"z:\\yay.jpg")
