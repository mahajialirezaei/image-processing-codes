import numpy as np


def getinput():
    n = int(input())
    a = []
    for i in range(n):
        a.append([])
        a[i] = list(map(float, input().split()))
    return a

if __name__ == '__main__':
    a = getinput()
    print(a)

