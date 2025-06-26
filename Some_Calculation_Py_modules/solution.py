import numpy as np
import math

def eigen_finder(A: np.ndarray):
    return list() if A.shape[0] != A.shape[1] else np.linalg.eigvals(A)


def frobenious_norm_finder(A: np.ndarray):
    return np.linalg.norm(A, 'fro')

def infinity_norm_finder(A: np.ndarray):
    return np.linalg.norm(A, math.inf)