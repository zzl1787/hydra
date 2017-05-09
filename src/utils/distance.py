import numpy as np

""" Calculates the euclidean distance between 2 lists of coordinates. """
def eucldist(vector1, vector2):
    return np.sqrt(np.sum((vector1 - vector2) ** 2))

