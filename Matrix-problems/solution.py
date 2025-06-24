from typing import Any

import numpy as np
from numpy import ndarray, dtype


def addition(m1:np.ndarray, m2:np.ndarray):
    try:
        m = np.add(m1, m2)
        return m
    except TypeError:
        return "Cannot be done"

