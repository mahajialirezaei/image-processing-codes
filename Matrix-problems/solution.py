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
    m_x = m1.shape[0] - m2.shape[0] + 1
    m_y = m1.shape[1] - m2.shape[1] + 1
    if m_x <= 0 or m_y <= 0:
        return "Cannot be done"
    m = []
    for i in range(m_x):
        m.append([])
        for j in range(m_y):
            m[i].append([])
            m1_s = m1[i: i+ m2.shape[0], j:j + m2.shape[1]]
            m[i][j] = np.sum(np.multiply(m1_s, m2))
    return np.array(m)
