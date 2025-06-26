import numpy as np
def eigen_finder(A: np.ndarray):
    return list() if A.shape[0] != A.shape[1] else np.linalg.eig(A)