import numpy as np

def addition(m1:np.ndarray, m2:np.ndarray):
    try:
        if m1.shape[0] != m2.shape[0] or m1.shape[1] != m2.shape[1]:
            raise Exception()
        m = np.add(m1, m2)
        return m
    except Exception as e:
        return "Cannot be done"

def subtraction(m1:np.ndarray, m2:np.ndarray):
    try:
        if m1.shape[0] != m2.shape[0] or m1.shape[1] != m2.shape[1]:
            raise Exception()
        m = np.subtract(m1, m2)
        return m
    except Exception as e:
        return "Cannot be done"

def multiply(m1:np.ndarray, m2:np.ndarray):
    try:
        if m1.shape[1] != m2.shape[0]:
            raise Exception()
        m = np.matmul(m1, m2)
        return m
    except Exception as e:
        return "Cannot be done"

def convolution(m1:np.ndarray, m2:np.ndarray):
    try:
        m = np.convolve(m1, m2, mode='valid')
        return m
    except Exception as e:
        return "Cannot be done"
