import numpy as np
import math

def eigen_finder(A: np.array):
    return list() if A.shape[0] != A.shape[1] else np.linalg.eigvals(A)


def frobenious_norm_finder(A: np.array):
    return np.linalg.norm(A, 'fro')

def infinity_norm_finder(A: np.array):
    return np.linalg.norm(A, math.inf)


def min_max_normalizer(A: np.array):
    A_min = np.min(A)
    A_max = np.max(A)

    A_min_max = (A-A_max)/(A_max-A_min)
    A_min_max = np.ndarray(A_min_max)
    return A_min_max