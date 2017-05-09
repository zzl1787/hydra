# coding:utf8
import os
import functools
from PIL import Image, ImageEnhance
from pytesser import image_to_string
import numpy as np
from src.config import configs
from pandas import DataFrame

dataframe = DataFrame(np.ones((4,4)))
dict1 = {}
#去掉全0行
rows = {}

