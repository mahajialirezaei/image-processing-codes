from typing import Any

import numpy as np
from numpy import ndarray, dtype


def addition(m1:np.ndarray, m2:np.ndarray):
    try:
        m = np.add(m1, m2)
        return m
    except TypeError:
        return "Cannot be done"

def subtraction(m1:np.ndarray, m2:np.ndarray):
    try:
        m = np.subtract(m1, m2)
        return m
    except TypeError:
        return "Cannot be done"

def multiply(m1:np.ndarray, m2:np.ndarray):
    try:
        m = np.multiply(m1, m2)
        return m
    except TypeError:
        return "Cannot be done"

def convolution(m1:np.ndarray, m2:np.ndarray):
    try:
        m = np.convolve(m1, m2)
        return m
    except TypeError:
        return "Cannot be done"
