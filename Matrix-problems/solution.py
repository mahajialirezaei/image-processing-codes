from typing import Any

import numpy as np
from numpy import ndarray, dtype


def addition(m1:np.ndarray, m2:np.ndarray):
    if m1.shape[0] != m2.shape[0] or m1.shape[1] != m2.shape[1]:
        raise TypeError()
    try:
        m = np.add(m1, m2)
        return m
    except TypeError:
        return "Cannot be done"

def subtraction(m1:np.ndarray, m2:np.ndarray):
    if m1.shape[0] != m2.shape[0] or m1.shape[1] != m2.shape[1]:
        raise TypeError()
    try:
        m = np.subtract(m1, m2)
        return m
    except TypeError:
        return "Cannot be done"

def multiply(m1:np.ndarray, m2:np.ndarray):
    if m1.shape[1] != m2.shape[0]:
        raise TypeError()
    try:
        m = np.multiply(m1, m2)
        return m
    except TypeError:
        return "Cannot be done"

def convolution(m1:np.ndarray, m2:np.ndarray):
    if m1.shape[0] != m2.shape[0] or m1.shape[1] != m2.shape[1]:
        raise TypeError()
    try:
        m = np.convolve(m1, m2, mode='valid')
        return m
    except TypeError:
        return "Cannot be done"
